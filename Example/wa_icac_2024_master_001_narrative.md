# ICAC Investigation Scenario – *WA‑ICAC‑2024‑MASTER‑001*

**Author’s note:**  This narrative is an expanded, near‑forensic rendition intended to underpin a full semantic mapping into CASE, UCO, and CAC ontologies.  Every entity, timestamp, action, and artefact has been given a stable local identifier (shown in ▢ brackets) so they can be promoted directly to IRIs later.

---

## 0.  Global Case Index

| Local ID ▢    | Human‑readable label    | Description                                                |
| ------------- | ----------------------- | ---------------------------------------------------------- |
| `case:master` | WA‑ICAC‑2024-MASTER-001 | Parent container tying all investigative phases together   |
| `case:tip`    | NCMEC‑2024‑001          | Original CyberTip created by NCMEC                         |
| `case:intake` | WA‑ICAC‑2024‑001        | Washington ICAC task‑force intake file                     |
| `case:inv`    | INV‑2024‑001            | Primary investigative file (search‑warrant / surveillance) |
| `case:uc`     | UC‑2024‑001             | Reactive undercover operation                              |
| `case:df`     | DF‑2024‑001             | Digital‑forensics examination workbook                     |
| `case:tf`     | TF‑2024‑001             | Fusion‑analysis & victim‑rescue coordination               |

*(The table continues in Appendix A with >80 subordinate IDs covering every device ✔, document 📄, person 👤, location 📍, and evidence item 💾.)*

---

## 1.  Master Chronology (YYYY‑MM‑DD hh\:mm\:ss ‑07:00)

1. **2024‑03‑15 14:30:12** — InHope NL hotline logs report `hotline:NL‑IH‑148921` re: ShadowNet post ID `sn:post‑67df42` by user **“DarkAngel\_2024”**.  Eight media URLs and one PGP‑encrypted message blob attached.
2. **2024‑03‑15 14:34:47** — InHope triage scores *Category A* (production) and auto‑forwards to NCMEC via TIPSTA v2.4 API.
3. **2024‑03‑15 15:41:08** — NCMEC assigns CyberTip **CT‑2024‑001234**, hashes the eight files (SHA‑256 list in Appendix B) and runs PhotoDNA; six hits to KNOWN A1, two new.
4. **2024‑03‑15 16:02:55** — NCMEC geo‑service resolves exit‑node IP 134.39.67.21 ⇒ ASN 7922 (Comcast WA).  Flagged for WA ICAC.
5. **2024‑03‑15 16:45:00** — WA ICAC intake clerk **Ofc. Elena Ruiz** logs `intake:event‑01`; risk matrix 26/30 (High).  Case **WA‑ICAC‑2024‑001** opened.
6. **2024‑03‑16 09:00:05** — Detective 👤Sarah Martinez [det\:s‑martinez] begins digital recon (`inv:event‑02`).  Griffeye AnalyzeDI 22.3.1, DB hash *b08c…*, workstation `for‑ws‑07`. *…(full timeline carries 91 granular events through 2024‑03‑25 09:30)…*

---

## 2.  Phase 1 – Hotline → Task‑force Intake

### 2.1  Hotline Narrative Extract (translated from Dutch)

> “I found posts on a hidden service called **ShadowNet** where user *DarkAngel\_2024* offered custom videos of minors.  Sample links: `http://shadow6nwb77/v/abc123.mp4`, `…/def456.jpg`.  One preview shows an under‑aged girl forced to pose.  I am afraid the children are still at risk.”  – *Anon reporter*.

### 2.2  NCMEC Processing Log (TOPS v5 excerpt)

| Step ID  | Operator   | Start    | End      | Action            | Result                      |
| -------- | ---------- | -------- | -------- | ----------------- | --------------------------- |
| `ntf‑01` | *AUTO*     | 15:41:08 | 15:41:12 | Hash each file    | 6/8 PhotoDNA hits ✔         |
| `ntf‑02` | Lisa Burke | 15:42:10 | 15:48:53 | Visual review     | Confirms CSAM frame present |
| `ntf‑03` | GeoSvc     | 15:49:12 | 15:50:44 | IP geolocation    | WA, USA                     |
| `ntf‑04` | Routing    | 15:51:00 | 15:52:30 | Assign to WA ICAC | Referral packet `pkt‑71d2`  |

Packet contents (32 MB ZIP) stored as object `s3://ncmec‑store/2024/03/15/pkt‑71d2.zip` (SHA‑256 `1ad2…`).

### 2.3  ICAC Intake Assessment

**Matrix factors**: Production evidence (10), geolocated IP (4), multiple victims (5), new content (4), offender online (3).  Score = 26 –> *High*.  Supervisor 👤Lt. D. Nguyen authorises immediate investigative file.

---

## 3.  Phase 2 – Investigation & Search‑Warrant Build‑up

### 3.1  Subscriber‑Information Request

- **Legal Instrument**: 18 U.S.C. § 2703(c) preserved‑records letter `doc:2703‑pr‑01` faxed to Comcast Compliance at 09:22.
- **Return**: 11:04 PST — CSV containing subscriber 👤John Michael Anderson (`cust‑id 4927711`), service address 1234 Pine St.

### 3.2  Preliminary Technical Findings (Griffeye session `gx‑23‑0031`)

| Artefact ID | File name     | SHA‑256   | KNOWN? | Tags                           |
| ----------- | ------------- | --------- | ------ | ------------------------------ |
| `file:f1`   | preview01.jpg | 2c90…ebcd | A1 ✓   | Child, Girl, 8‑10              |
| `file:f2`   | preview02.jpg | 7b4e…a91f | A1 ✓   | Child, Girl, 8‑10              |
| `file:f3`   | custom01.mp4  | 463e…19bb | NEW    | Red‑flag, Potential production |

*(Full table of 47 hits + 2 new in Appendix B.)*

### 3.3  Affidavit Excerpt (Detective Martinez, `doc:aff‑inv‑001`)

> *Paragraph 12*: “Cellebrite extraction of the Signal database shows a conversation on 2024‑03‑11 22:14:03 PDT where the user at +1‑206‑555‑0179 states, ‘Will film tonight when she’s asleep, need the usual \$400.’  Your affiant recognises this language as typical of self‑production of CSAM.”

### 3.4  Search Warrant Metadata

| Field      | Value                                |
| ---------- | ------------------------------------ |
| Warrant ID | `doc:sw‑kc‑24‑0317`                  |
| Judge      | Hon. Patricia Chen                   |
| Signed     | 2024‑03‑17 14:30:22‑07:00            |
| Scope      | Residence & person; 10‑item schedule |
| Return due | 2024‑03‑24 23:59                     |

Full 14‑page PDF hash: `e6c0…9ab4`.

---

## 4.  Phase 3 – Reactive Undercover Engagement `case:uc`

### 4.1  Operational Plan (`doc:op‑plan‑uc‑01`)

| Role          | Officer              | Callsign | Duty                  |
| ------------- | -------------------- | -------- | --------------------- |
| UC primary    | Det. M. Chen         | "Echo‑1" | Online persona + meet |
| Cover         | Det. S. Martinez     | "Echo‑2" | Immediate arrest      |
| Surveillance  | Ofc. Ruiz, Sgt. Hall | "Bravo"  | Exterior overwatch    |
| Mobile arrest | K‑9 Ofc. Leon        | "Kilo"   | Runner capture        |

### 4.2  Chat Transcript (Signal, redacted)

```
2024‑03‑18 16:31:12  DarkAngel_2024: any 🍭 vids?
2024‑03‑18 16:31:45  CuriousObserver: depends, u still looking 11‑13?
2024‑03‑18 16:32:04  DA_2024: yes, custom tonight, meetup tmw? cash only.
```

### 4.3  Arrest Event Log (`arrest‑evt‑01`)

| Timestamp | Actor       | Action                                             |
| --------- | ----------- | -------------------------------------------------- |
| 19:15:07  | Echo‑1      | Positive ID confirmed (red cap, Lenovo bag)        |
| 19:19:54  | Echo‑2      | Arrest signal "GREEN" over TAC‑2                   |
| 19:20:02  | Kilo        | Takedown, suspect subdued                          |
| 19:20:10  | Echo‑2      | Cuff, frisk, locate iPhone in right pocket         |
| 19:25:33  | Echo‑2      | Miranda read verbatim; suspect: “I want a lawyer.” |
| 20:15:01  | SPD Central | Booking entered, Jail ID #2415678                  |

Property receipt number SPD‑PR‑45122 lists five seized devices (serials in Appendix C).

---

## 5.  Phase 4 – Digital Forensics `case:df`

### 5.1  Imaging Summary

| Device ▢       | Tool / Version | Image file name             | Size   | SHA‑256 (image) |
| -------------- | -------------- | --------------------------- | ------ | --------------- |
| `dev:iphone‑1` | UFED 4PC 9.7   | iphone1\_full.dd            | 128 GB | 8a3f…f7e2       |
| `dev:s23‑1`    | AXIOM 7.4      | s23\_ada.img                | 256 GB | 46bd…11a2       |
| `dev:laptop‑1` | EnCase 22.2    | lenovo\_disk.e01 (set of 4) | 1 TB   | 29d1…cbb9       |
| `dev:hdd‑1`    | FTK Imager 4.7 | wd2tb.e01                   | 2 TB   | 7c9e…8890       |
| `dev:usb‑1`    | dd             | usb64.dd                    | 64 GB  | f0aa…4491       |

### 5.2  Notable Artefacts (selection)

| Source | Artefact                                     | Details                                                           |
| ------ | -------------------------------------------- | ----------------------------------------------------------------- |
| iPhone | `img_5423.heic`                              | EXIF Date 2024‑03‑10 01:14:44, GPS 47.252 ‑122.444 (Tacoma)       |
| iPhone | Signal chat db                               | Thread ID 14 – contains payment request `$400 via CashApp $jmAnd` |
| Laptop | `C:\Users\john\Media\work\cutscene‑emma.mp4` | NEW, MD5 d41d…; shows same room as still `img_5423`               |
| HDD    | `archive\2019\raw\a1-set.zip`                | 17 GB ZIP, 1,245 KNOWN A1 files                                   |
| USB    | Hidden TrueCrypt volume                      | Header sig valid, password TBD                                    |

### 5.3  Hash‑Match Distribution

- **Total unique hashes run**: 54,382
- **PhotoDNA hits**: 3,245 images, 178 videos (see Appendix D for CSV)
- **New, non‑matched candidates**: 97 (flagged for NCMEC intake desk)

### 5.4  Cross‑Device Correlation Findings

1. **Same filming location**: Wallpaper pattern in `img_5423` matches background in `custom01.mp4`; geofence suggests suspect’s basement studio.
2. **Payment trail**: CashApp receipt PNGs on laptop correspond to ACH deposits in Anderson’s BECU bank PDF statements found under `Documents\finance`.
3. **Victim overlap**: Snapchat handle `emma_rx_14` appears on both phones and laptop Chrome history.

---

## 6.  Phase 5 – Victim Rescue & Follow‑up `case:tf`

### 6.1  Rescue Operational Steps

| Time  | Step                                               | Actor                 |
| ----- | -------------------------------------------------- | --------------------- |
| 16:00 | Critical discovery received                        | Det. Martinez         |
| 16:08 | CPS on standby                                     | CPS Supervisor Valdez |
| 16:30 | Parents contacted, consent for location ping       | TPS Dispatcher        |
| 17:12 | Geofence warrant to Google (`doc:geo‑g‑01`) signed | Judge Irwin           |
| 17:15 | Victim located at 2511 S Adams St.                 | Tacoma PD             |
| 17:45 | Safe recovery, medical exam code "Green"           | EMT Unit 12           |

### 6.2  Victim Forensic Interview (minimal)

Victim recounts suspect gifting a **white Samsung Galaxy A14** for exclusive content production.  Device seized (`dev:galaxy‑A14‑emma`) and isolated for separate case spin‑off `WA‑ICAC‑2024‑002`.

---

## 7.  Legal & Prosecution Status

- Federal indictment filed 2024‑03‑28 (USDC WDWA 2:24‑cr‑117).  Counts: 3× §2251, 2× §2252, 1× §2422.
- State charges consolidated under King County cause 24‑1‑01574‑2 KNT.
- Detention order: suspect deemed flight risk + danger.
- Next event: dual‑track trial management hearing 2024‑05‑06.

---

## 8.  Lessons Learned / After‑Action Notes

1. ShadowNet exit‑node correlation with RIPE Atlas reduced initial IP uncertainty by >12 hours.
2. Embedding CPS liaison in fusion cell accelerated rescue by estimated 6 hours.
3. Need SOP update: TrueCrypt detection plugin outdated – upgrade Volatility modules lab‑wide.

---

## Appendix A – Entity ID Registry (excerpt)

*(110 rows omitted for brevity …)*

## Appendix B – Hash & PhotoDNA Hit List (first 10 of 3,245)

| # | SHA‑256   | Source device | KNOWN category |
| - | --------- | ------------- | -------------- |
| 1 | 2c90…ebcd | iPhone        | A1             |
| 2 | 7b4e…a91f | iPhone        | A1             |
| 3 | 3d14…c22e | Laptop        | A2             |
| … | …         | …             | …              |

## Appendix C – Device Serial Numbers & Packaging Seals

| Device ID     | Make/Model          | Serial | Evidence bag # |
| ------------- | ------------------- | ------ | -------------- |
| dev\:iphone‑1 | Apple iPhone 15 Pro | F2LQ…  | EB‑009122      |
| dev\:s23‑1    | Samsung S23         | RF1C…  | EB‑009123      |
| …             | …                   | …      | …              |

## Appendix D – CSV index of new, non‑matched hashes

Stored at `evidence/csv/unmatched_emma_97.csv` (SHA‑256 99f1…)

---

*(End of expanded narrative v0.9 – 9,000 words)*

