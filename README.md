# Security Lab Practice

[![Python 3](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![PHP](https://img.shields.io/badge/PHP-7%2F8-orange.svg)](https://www.php.net/)
[![Status](https://img.shields.io/badge/Status-Learning%20Only-orange.svg)](#security-notes)
[![Use responsibly](https://img.shields.io/badge/Use-Authorized%20Lab%20Only-red.svg)](#security-notes)

![Security Lab Practice Banner](docs/screenshots/banner.svg)

A small educational repository for practicing local network and shell basics in a controlled lab environment.

This project includes:
- a minimal local HTTP file server
- a simple reverse-shell example template
- a PTY upgrade snippet for learning about interactive shells

## Security notes

This repository is intended strictly for:
- authorized lab environments
- local virtual machines you own or control
- educational or training scenarios with explicit permission

Do not run these scripts against:
- production systems
- external hosts without permission
- any target outside an approved testing environment

## Repository layout

```text
security-lab-practice/
├── README.md
├── .gitignore
├── examples/
│   ├── http_server/
│   │   └── simplehttpser.py
│   └── reverse_shell/
│       └── simpleRevShell.php
├── notes/
│   ├── pty-upgrade.md
│   └── security-lab-notes.md
├── docs/
│   └── screenshots/
│       ├── banner.svg
│       ├── http-server-usage.svg
│       └── pty-upgrade.svg
└── legacy/
    └── old_examples/
```

## Quick start

### 1) Start the local HTTP server

```bash
python3 examples/http_server/simplehttpser.py
```

This starts a minimal local web server on port 8080. Open your browser to:

```text
http://127.0.0.1:8080/
```

![HTTP server usage](docs/screenshots/http-server-usage.svg)

### 2) Reverse-shell example template

This is a template for learning how reverse-shell payloads are structured in a controlled lab environment.

```php
<?php
// Example lab-only template
// Replace the host/port values to match your isolated environment.
// NEVER run this against unauthorized systems.
$host = "127.0.0.1";
$port = 8080;
?>
```

### 3) Upgrade a basic shell to a PTY shell

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

The PTY upgrade helps a shell behave more like an interactive terminal. This is useful in a lab for studying terminal behavior and shell upgrades.

![PTY upgrade example](docs/screenshots/pty-upgrade.svg)

## Usage

This repo is useful for learning:
- how a local HTTP listener works
- how a reverse-shell payload is structured
- how PTY upgrades make a shell more usable
- how to inspect and map basic network and shell behaviors in a controlled lab

### Typical lab flow

1. Run the simple HTTP server locally.
2. Study the listener flow and port behavior.
3. Review the reverse-shell template in a controlled environment.
4. Practice the PTY upgrade workflow in a VM or lab system.
5. Record findings in the notes folder.

## Notes

See:
- `notes/pty-upgrade.md`
- `notes/security-lab-notes.md`

## License status

This repository does not currently include a project license. It is intended for educational use in authorized lab environments only.
