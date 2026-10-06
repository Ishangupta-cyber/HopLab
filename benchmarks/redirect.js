import http from "k6/http";
import { check } from "k6";


const CODE = __ENV.CODE;
if (!CODE) {
  throw new Error("Short code do: k6 run -e CODE=xxxx benchmarks/redirect.js");
}

export const options = {
  vus: 50,
  duration: "30s",
  thresholds: {
    checks: ["rate>0.99"],     // 99% se kam sahi → test FAIL mark hoga
  },
};

export default function () {
  const res = http.get(`http://localhost:8000/${CODE}`, { redirects: 0 });
  check(res, { "is 302": (r) => r.status === 302 });
}