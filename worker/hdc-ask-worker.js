/**
 * HDC Wiki "Ask" backend — a Cloudflare Worker that answers chat questions with Workers AI.
 *
 * The website (GitHub Pages) finds the relevant wiki passages itself and sends them here with the
 * question; this Worker only forwards them to the model and streams the answer back.
 * No API key is stored anywhere: the model runs on Cloudflare through the "AI" binding.
 *
 * Setup (Cloudflare dashboard): Workers & Pages -> Create -> Worker -> paste this file -> Deploy,
 * then Settings -> Bindings -> Add -> Workers AI, variable name: AI -> Deploy.
 */
const ALLOWED_ORIGINS = [
  "https://conslmhoang.github.io",
  "http://localhost:8765",
];
const MODEL = "@cf/meta/llama-3.3-70b-instruct-fp8-fast";
const MAX_INPUT_CHARS = 40000;

function cors(origin) {
  const ok = ALLOWED_ORIGINS.includes(origin);
  return {
    "Access-Control-Allow-Origin": ok ? origin : ALLOWED_ORIGINS[0],
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Vary": "Origin",
  };
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || "";
    if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: cors(origin) });
    if (request.method !== "POST") return new Response("HDC Wiki ask endpoint. POST {messages}.", { headers: cors(origin) });
    if (!ALLOWED_ORIGINS.includes(origin)) return new Response("Origin not allowed", { status: 403, headers: cors(origin) });

    let body;
    try { body = await request.json(); } catch { return new Response("Bad JSON", { status: 400, headers: cors(origin) }); }
    const messages = Array.isArray(body.messages) ? body.messages
      .filter(m => m && ["system", "user", "assistant"].includes(m.role) && typeof m.content === "string")
      .slice(-8) : [];
    const size = messages.reduce((n, m) => n + m.content.length, 0);
    if (!messages.length || size > MAX_INPUT_CHARS) return new Response("Message missing or too long", { status: 413, headers: cors(origin) });

    try {
      const stream = await env.AI.run(MODEL, { messages, stream: true, max_tokens: 900, temperature: 0.2 });
      return new Response(stream, { headers: { ...cors(origin), "Content-Type": "text/event-stream", "Cache-Control": "no-store" } });
    } catch (e) {
      const msg = String(e && e.message || e);
      const status = /limit|quota|neuron|429/i.test(msg) ? 429 : 502;
      return new Response(msg, { status, headers: cors(origin) });
    }
  },
};
