# Public preview test fixture

Small, synthetic Python project for testing code review and scan workflows.
It contains no customer code, credentials, private data, or production services.

Run the deterministic tests with `python3 -m unittest discover -s tests`.
The project has no network access or third-party dependencies.

Automatic pull-request reviews are disabled. Test runs are triggered explicitly.
