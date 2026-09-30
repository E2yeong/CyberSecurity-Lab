# Cybersecurity Study Notes

Notes I wrote while studying cybersecurity: networking and Linux basics, cryptography and TLS, and common attacks seen from the defender's side. Most were first posted on my [Naver blog](https://blog.naver.com/ddak_sound) in Korean and rewritten here in English.

**Read them online:** https://e2yeong.github.io/CyberSecurity-Lab/

The code projects that grew out of these notes (a password strength checker and a SHA-256 vs Argon2id hasher) now live in their own repository: **[password-security-toolkit](https://github.com/E2yeong/password-security-toolkit)**.

> Offensive techniques are described at a conceptual level for authorized lab practice and defense. No exploit code or step-by-step intrusion instructions are included.

## Notes

### Foundations

| # | Note | Posted |
|---|---|---|
| 01 | [What is Hacking?](https://e2yeong.github.io/CyberSecurity-Lab/notes/01-what-is-hacking/) | 2024-10-30 |

### Networking & Linux

| # | Note | Posted |
|---|---|---|
| 02 | [What is a Network?](https://e2yeong.github.io/CyberSecurity-Lab/notes/02-what-is-a-network/) | 2024-11-06 |
| 03 | [Why Hackers Use Linux](https://e2yeong.github.io/CyberSecurity-Lab/notes/03-why-hackers-use-linux/) | 2024-11-13 |
| 04 | [Basic Linux Commands](https://e2yeong.github.io/CyberSecurity-Lab/notes/04-basic-linux-commands/) | 2024-11-22 |
| 05 | [Network Hacking: Concepts, Setup, and Safer Practices](https://e2yeong.github.io/CyberSecurity-Lab/notes/05-network-hacking-concepts/) | 2024-11-27 |
| 06 | [MAC Address: Concept, Spoofing, and Security](https://e2yeong.github.io/CyberSecurity-Lab/notes/06-mac-address-spoofing/) | 2024-12-04 |
| 07 | [Monitor Mode & Packet Sniffing (Wi-Fi)](https://e2yeong.github.io/CyberSecurity-Lab/notes/07-monitor-mode-packet-sniffing/) | 2025-01-22 |
| 08 | [Gaining Access: Server, Client and External Vectors (Defensive Guide)](https://e2yeong.github.io/CyberSecurity-Lab/notes/08-gaining-access-defensive-guide/) | 2025-07-23 |

### Passwords & Cryptography

| # | Note | Posted |
|---|---|---|
| 09 | [Password Vulnerabilities and Best Practices](https://e2yeong.github.io/CyberSecurity-Lab/notes/09-password-vulnerabilities/) | 2025-08-29 |
| 10 | [Password Hashing: From Data Structures to Secure Storage](https://e2yeong.github.io/CyberSecurity-Lab/notes/10-password-hashing/) | 2025-09-04 |
| 11 | [Symmetric Encryption & AES](https://e2yeong.github.io/CyberSecurity-Lab/notes/11-symmetric-encryption-aes/) | 2024-09-11 |
| 12 | [Asymmetric Encryption (RSA, ECC, Diffie–Hellman)](https://e2yeong.github.io/CyberSecurity-Lab/notes/12-asymmetric-encryption/) | 2024-09-18 |
| 13 | [SSL/TLS & HTTPS](https://e2yeong.github.io/CyberSecurity-Lab/notes/13-tls-and-https/) | 2024-09-25 |
| 14 | [Why Your Browser Shows a Padlock: Understanding PKI](https://e2yeong.github.io/CyberSecurity-Lab/notes/14-pki-browser-padlock/) | 2024-10-20 |

### Threats & Defense

| # | Note | Posted |
|---|---|---|
| 15 | [Network & Security: From Fundamentals to Defense](https://e2yeong.github.io/CyberSecurity-Lab/notes/15-network-security-fundamentals/) | 2025-10-20 |
| 16 | [Malware: Types, Evolution, and Detection](https://e2yeong.github.io/CyberSecurity-Lab/notes/16-malware/) | 2025-10-23 |
| 17 | [Social Engineering: The Human Side of Cybersecurity](https://e2yeong.github.io/CyberSecurity-Lab/notes/17-social-engineering/) | 2025-11-06 |

## Repository layout

```
index.html              list of all notes (the GitHub Pages home page)
notes/NN-topic/         one folder per note, numbered in reading order
404.html                forwards old URLs from the previous folder layout
```

Each note is a single self-contained HTML page with Back / Next links in reading order. Old links (for example from blog posts) that used the previous nested folder layout are redirected to the new pages by `404.html`.

To read offline, clone the repository and open `index.html` in a browser.

## Related

- [password-security-toolkit](https://github.com/E2yeong/password-security-toolkit): strength checker and hasher built from notes 09 and 10
- [ComputerScience](https://github.com/E2yeong/ComputerScience): algorithms and the number theory behind RSA
- [Portfolio](https://e2yeong.github.io/my-portfolio/)
