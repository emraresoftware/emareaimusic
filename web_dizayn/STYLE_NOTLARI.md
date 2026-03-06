# Emare AI Music — Tasarım Rehberi (Design System)

> Otomatik oluşturuldu: emarework Dervishi — Çeyiz Sistemi
> Ana Renk: `#10b981`
> Tarih: 06 March 2026

---

## 1. RENK PALETİ (Brand Colors)

| Token | HEX | Kullanım |
|-------|-----|----------|
| `brand-50` | `#f4f9f8` | Çok açık arka plan, hover bg |
| `brand-100` | `#e9f6f1` | Açık arka plan |
| `brand-200` | `#c7eee1` | Border (secondary buton) |
| `brand-300` | `#90e9cb` | İkon accent |
| `brand-400` | `#54e7b6` | Hover accent |
| `brand-500` | `#14eaa3` | **Ana marka rengi (Primary)** |
| `brand-600` | `#11c589` | Hover/active primary |
| `brand-700` | `#0aa370` | Koyu primary |
| `brand-800` | `#077c56` | Koyu bg accent |
| `brand-900` | `#07543a` | Çok koyu bg |
| `brand-950` | `#052d20` | En koyu bg (hero, footer) |

---

## 2. GRİ TONLARI

| Token | Kullanım |
|-------|----------|
| `white` | Sayfa arka planı, kart arka planı |
| `gray-100` | Border, divider |
| `gray-300` | Footer body text |
| `gray-500` | Kart açıklamaları |
| `gray-600` | Body paragraph text |
| `gray-800` | Varsayılan metin |
| `gray-900` | Başlıklar |
| `gray-950` | Footer arka plan |

---

## 3. EK RENKLER

| Renk | HEX | Kullanım |
|------|-----|----------|
| Success | `#22c55e` | Başarı, onay |
| Warning | `#f59e0b` | Uyarı |
| Error | `#ef4444` | Hata |
| Info | `#3b82f6` | Bilgi |

---

## 4. GRADYANLAR

### Primary Buton
```css
background: linear-gradient(to right, #14eaa3, #0aa370);
```

### Gradient Text
```css
background: linear-gradient(135deg, #11c589, #54e7b6);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
```

### Hero Koyu Arka Plan
```css
background: linear-gradient(-45deg, #052d20, #07543a, #077c56);
```

---

## 5. TİPOGRAFİ

| Element | Font | Size | Weight |
|---------|------|------|--------|
| H1 | Inter | 3rem (48px) | 800 (ExtraBold) |
| H2 | Inter | 2.25rem (36px) | 700 (Bold) |
| H3 | Inter | 1.5rem (24px) | 600 (SemiBold) |
| Body | Inter | 1rem (16px) | 400 (Regular) |
| Small | Inter | 0.875rem (14px) | 400 |
| Button | Inter | 0.875rem (14px) | 600 |

---

## 6. SPACING

| Token | Değer | Kullanım |
|-------|-------|----------|
| xs | 4px | İkon-metin arası |
| sm | 8px | Küçük aralık |
| md | 16px | Kart padding |
| lg | 24px | Bölüm arası |
| xl | 48px | Büyük bölüm arası |
| 2xl | 96px | Hero section padding |

---

## 7. TAILWIND CONFIG

```javascript
tailwind.config = {
  theme: {
    extend: {
      fontFamily: { sans: ['Inter', 'system-ui', 'sans-serif'] },
      colors: {
        brand: {
          50: '#f4f9f8',
          100: '#e9f6f1',
          200: '#c7eee1',
          300: '#90e9cb',
          400: '#54e7b6',
          500: '#14eaa3',
          600: '#11c589',
          700: '#0aa370',
          800: '#077c56',
          900: '#07543a',
          950: '#052d20',
        }
      }
    }
  }
}
```

---

*Otomatik oluşturuldu — emarework Dervishi Çeyiz Sistemi*
