# Provenance & Timestamp Plan
Goal: prove each post's authorship and publish-time indefinitely.

Workflow summary:
1. Bundle edition (post + metadata + audio) → SHA-256 hash.  
2. Sign hash via hardware-key (YubiKey/GPG).  
3. Obtain **Danish QTSP Qualified Timestamp (.tsr)** for legal timeproof.  
4. (Optional) Anchor hash with **OpenTimestamps (.ots)** for Bitcoin proof.  
5. Pin edition bundle on self-hosted **IPFS node (DK)** → CID.  
6. Store metadata + artifact URLs in Supabase (`post_editions` table).  
7. Each post displays a **ProofPanel** listing:
   - UTC publish time  
   - SHA-256 hash  
   - Signature (fingerprint + link)  
   - QTST token link  
   - OTS proof link (if any)  
   - IPFS CID link (immutable copy)  
   - "Verify this edition" CTA → `/verify`
8. `/verify` page recomputes hash, validates signature, QTST, OTS.

Technical Implementation:
- Use Python `cryptography` library for SHA-256 hashing
- Use `python-gnupg` for GPG signature verification
- Use `ipfshttpclient` for IPFS operations
- Store artifacts on Railway volumes or Supabase Storage

Court-strength proofs rely on Danish QTSP + your key + IPFS retrievability.  
Everything must remain free or hosted in Denmark.

