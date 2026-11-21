# Types of Attack — Project Aurora

> Prezentare de ansamblu a tipurilor de atac folosite în proiect, pe maparea canonică
> **taxonomie → modul atacator → clasă ML** (vezi `CLAUDE.md`).
>
> **Scop educațional, exclusiv în lab izolat** (rețea separată, fără internet, fără ținte reale).
> Singura țintă permisă este Pi-ul propriu din lab (IP din `config/lab.yaml`).
>
> Explicația detaliată „ce face exact fiecare atac" (mecanism + semnătură de trafic) este în
> documentul privat `docs-private/taxonomie/atacuri_detaliat.md`.

**Principiu:** rostul atacurilor nu e să „spargă" Pi-ul, ci să genereze **trafic etichetat, cu
semnături distincte**, pe care modelul ML (Random Forest) să le clasifice. Alegem algoritmi care
produc semnături clare per clasă.

---

## 1. `recon.py` → `PORTSCAN`
Scanare / recunoaștere. Semnătură: multe conexiuni scurte spre multe porturi.
- **TCP SYN scan** (half-open) — cel mai distinct.
- **TCP connect scan** (handshake complet).
- **FIN / NULL / Xmas scan** (flag-uri neobișnuite).
- **UDP scan**.
- **Ping sweep** (ICMP echo / ARP discovery local).
- **OS & service fingerprinting** + **banner grabbing**.
- Variabilă cheie: **timing** (nmap `-T0..-T5`).
- Tool-uri: `nmap` și/sau pachete hand-crafted cu **scapy**.

## 2. `dos.py` → `DDOS`
Denial of Service. Semnături foarte diferite între volumetric și low-and-slow.
- **Volumetrice:** SYN flood, UDP flood, ICMP flood.
- **Application-layer (low-and-slow):** Slowloris, slow POST, HTTP GET/POST flood.
- Tool-uri: `hping3`, scapy, Slowloris propriu.
- ⚠️ Pi 2 GB: țintim *demonstrarea semnăturii*, nu doborârea; reglăm rata ca să nu afectăm senzorul/inferența.

## 3. `auth.py` → `BRUTEFORCE`
Atac pe credențiale. Semnătură: multe încercări de login într-un timp scurt.
- **Brute force** (exhaustiv), **dictionary attack**.
- **Password spraying** (o parolă × mulți useri).
- **Credential stuffing**, **default credentials**.
- Ținte: SSH, formular login HTTP.
- Tool-uri: `hydra`, sau paramiko/requests propriu.

## 4. `web.py` → `WEB_ATTACK`
Exploatare web. Semnătură: payload-uri în URL/body/headere.
- **SQLi** (union / error / boolean-time blind).
- **XSS** (reflected / stored / DOM).
- **Command injection**, **path traversal**, **file upload** malițios, **SSRF**.
- Tool-uri: payload-uri manuale cu `requests`; eventual `sqlmap` ca referință.
- Ținta web: aplicație **Flask vulnerabilă proprie** (ușoară pt. 2 GB), nu DVWA.

## 5. `spoofing.py` → `SPOOFING` *(iterația 2 — contribuție originală)*
- **ARP spoofing / cache poisoning** → MITM. **Clasa ML nouă**, pe date proprii.
- **DNS spoofing** și **IP spoofing** → demonstrații (fără clasă ML, deocamdată).
- Tool-uri: **scapy** (hand-crafted — aportul tehnic al lucrării).
- Semnătură: binding **MAC↔IP duplicat / anormal** → baseline heuristic de comparat cu ML.

---

## Ordinea de construcție (din planificare)
- **Faza 4 (fir vertical):** un singur algoritm per clasă (ex. SYN scan pentru `PORTSCAN`), cap-coadă.
- **Faza 5:** restul variantelor, pentru diversitate de semnături și dataset propriu mai bogat.

| Modul | Clasă ML | Faza |
|---|---|---|
| `recon.py` | `PORTSCAN` | 4 (fir vertical) |
| `dos.py` | `DDOS` | 5 |
| `auth.py` | `BRUTEFORCE` | 5 |
| `web.py` | `WEB_ATTACK` | 5 |
| `spoofing.py` | `SPOOFING` | iterația 2 |
