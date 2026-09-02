# Black-box Skill scenarios

`scenarios.json` defines fresh-session Harness cases. Runner puts `stub-horizon` on `PATH` as `horizon`, points `HORIZON_STUB_STATE` at case `stub` JSON, captures `HORIZON_STUB_LOG`, invokes `horizon` Skill with case prompt, and grades observable questions, guidance, stop points, and command trace against `expect`.

`missing-cli` omits stub from `PATH`. Multi-turn cases return listed `userReplies` in order. No scenario supplies credentials to Agent context. `python3 tests/verify.py` validates suite and stub responses without model calls.
