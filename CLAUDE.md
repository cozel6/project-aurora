# CLAUDE.md — Project Aurora

> ## ⚠️ DISCLAIMER
>
> **Scop exclusiv educațional.** Acest proiect este o lucrare de licență. Tot ce ține de testarea
> securității (recon, atacuri, spoofing etc.) se execută **strict local, într-un lab izolat**, pe
> echipamentul propriu (Raspberry Pi din lab), fără acces la internet și fără ținte reale. **Nu** este
> destinat și **nu** trebuie folosit împotriva vreunui sistem, rețea sau persoană fără autorizare. Atât.
>
> **Despre AI și autoratul codului.** Unele fișiere din proiect au fost sau vor fi realizate cu
> ajutorul inteligenței artificiale (documentare, structură, idei, ghidare). Totuși, **tot codul este
> și trebuie să rămână scris de mână** de autor — uneori sub îndrumarea asistentului AI, dar niciodată
> generat și lipit „la pachet". AI-ul are rol de mentor/consultant, nu de autor al codului.

Proiect de licență, scop educațional, lab izolat.

Reguli de bază:

- 3 mașini din același repo: **PC** și **Mac** (dezvoltare + atacator + antrenare ML), **Raspberry Pi 4 (2 GB)** (server victimă + senzor + inferență + răspuns).
- Antrenarea ML doar pe PC/Mac; pe Pi doar inferență. **Fără TensorFlow/PyTorch pe Pi.**
- Nu comite și nu face push decât dacă îți cer explicit.
- Cod de atac doar împotriva Pi-ului din lab-ul izolat (IP din `config/lab.yaml`).
- **Mod de lucru cu codul:** explică, ghidează, propune structuri și pseudocod, review la ce scriu eu.
  Nu-mi livra fișiere de cod gata făcute „la pachet" decât dacă cer explicit; codul îl scriu de mână.
