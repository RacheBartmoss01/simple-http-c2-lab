# Simple Local Security Practice Scripts

This repository contains a few very small example scripts for learning about:
- hosting a simple HTTP service locally
- how reverse-shell payload patterns are structured in a lab environment
- upgrading a basic shell into a more interactive PTY session

Important:
- These scripts are intended for authorized, isolated, learning environments only.
- Only use them on systems you own or have explicit written permission to test.
- Do not run them against production systems, shared networks, or external targets without authorization.

## Use cases

1. Local web hosting practice
   - Serve a folder or simple page from your own machine
   - Useful for learning HTTP basics, ports, listeners, and local testing workflows

2. Learning lab for command-and-control patterns
   - Use as a code example for understanding how a client connects back to a listener
   - Helps with learning payload structure and network flow in a controlled lab setup

3. Shell upgrade practice
   - Demonstrates how a basic shell can be upgraded to a more interactive PTY-based prompt
   - Useful for understanding shell behavior and TTY/PTY basics

## Files in this repository

- `simplehttpser.py` — starts a simple local HTTP server on port 8080
- `simpleRevShell.php` — example reverse-shell pattern template for learning in authorized lab use only
- `upgradetty.txt` — example PTY upgrade snippet for shell usability

## Quick start

### Start the local HTTP server
```bash
python3 simplehttpser.py
```
Then open your browser to:
```text
http://127.0.0.1:8080/
```

### Example reverse-shell pattern
This file is intentionally a template/example for a lab environment only. Replace placeholders before using in any controlled test environment.

```php
<?php
// Authorized lab use only.
// Replace the placeholder IP/PORT with values used in your own isolated environment.
// Example pattern only — do not use against unauthorized systems.
$host = "127.0.0.1";
$port = 8080;
$command = "/bin/sh";
// Example structure only; adapt for your own isolated lab setup.
?>
```

### Upgrade a shell to PTY
```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

## Notes

This repository is meant as a learning and security-practice project. It is best used in:
- local virtual machines
- isolated lab networks
- training environments with explicit permission

Use responsibly and ethically.
