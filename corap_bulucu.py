#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rüyada Kaybolan Çorap Bulucu
Dünyanın en ciddi yazılımı.
"""

import random
import time

def corap_bul(renk, boyut):
    """Çorabı rüyada bulur. Gerçekten."""
    print("\n🔍 Rüya tarama başlatılıyor...")
    time.sleep(1.5)
    
    konumlar = [
        "Sol cebinizin arkasında, 1997 yılının bir çarşamba gününde",
        "Büyükannenizin rüyasının en karanlık köşesinde",
        "Zaman yolcusunun unuttuğu çamaşır makinesinde",
        "Evrenin merkezinde, ama sadece siz bakarken",
        "Sağ ayakkabınızın içinde, ama ters dönmüş olarak",
        "Gelecekten gelen bir kargo kutusunun içinde"
    ]
    
    psikoloji = random.choice(["mutlu", "kızgın", "varoluşsal kriz içinde", "özgürlük arayan", "kayyum atanmış"])
    
    konum = random.choice(konumlar)
    
    print(f"\n✅ Çorap bulundu!")
    print(f"Renk: {renk}")
    print(f"Boyut: {boyut}")
    print(f"Konum: {konum}")
    print(f"Psikolojik durum: {psikoloji}")
    print(f"Doğruluk oranı: %{random.randint(99, 100)}")
    
    # Gizli not (base64 decode edilirse anlaşılır)
    # SGVyc2V5IGdlbGVuIGlsbGVyIGdlbGVuIGdldGlybWVsaWRpci4=
    
    return konum

if __name__ == "__main__":
    print("=" * 50)
    print("   RÜYADA KAYBOLAN ÇORAP BULUCU v1.0")
    print("   Kayyum onaylı resmi yazılım")
    print("=" * 50)
    
    renk = input("\nÇorabın rengi nedir? (rüyada): ") or "görünmez"
    boyut = input("Boyutu nedir? (küçük/orta/büyük/evren kadar): ") or "normal"
    
    corap_bul(renk, boyut)
    
    print("\n🎉 İşlem tamamlandı. Çorabınız artık güvende (veya değil).")
    print("\n---")
    print("İmza: Kayyum Grok | 03.11.2026 | Bu kod ciddiye alınmalıdır.")
    print("Eskişehir 4. Ağır Ceza Mahkemesi kayyum damgası ile mühürlenmiştir.")
