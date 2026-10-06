# Benchmark results

Load test: `k6 run -e CODE=<code> benchmarks/redirect.js` (50 VUs, 30s, `GET /<code>`, redirects not followed).

| Version | Setup | VUs | Throughput | p95 | Errors |
|---|---|---|---|---|---|
| v1-naive (smoke) | runserver, Windows | 50 | 121.8 req/s | 591 ms | 17.7% |
| v1-naive (official) | gunicorn 1 sync worker, Docker | 50 | 45.6 req/s | 1.17 s | 0% |

**Machine:** AMD Ryzen 5 5600H (6 cores / 12 threads), 15.4 GB RAM, Windows 11. k6 and Docker run on the same laptop, so they compete for CPU.

**Method:** the official row is the median of 3 runs (throughput 45.5 / 45.9 / 45.6 req/s, p95 1128 / 1170 / 1204 ms, 0% failed in all three). Raw k6 summaries are in `benchmarks/runs/`.

The smoke row is not a baseline: `runserver` is not a production server, and its 17.7% errors make the throughput and latency look better than they are. Failed requests return almost instantly, so they pull the average down. Read the `expected_response:true` duration and p95, not the plain average.

**Correctness check (v1):** 3,047 successful redirects under 50 concurrent users →
click_count increased by exactly 3,047. Atomic DB-side increment (F expression)
prevented lost updates.
