function RSAKeyPair(i, n, r, e) {
    this.e = biFromHex(i),
    this.d = biFromHex(n),
    this.m = biFromHex(r),
    "number" != typeof e ? this.chunkSize = 2 * biHighIndex(this.m) : this.chunkSize = e / 8,
    this.radix = 16,
    this.barrett = new BarrettMu(this.m)
}
function encryptedString(i, n, r, e) {
    var t, o, d, h, a, g, S, c, P, u, A = new Array, s = n.length, f = "";
    for (h = "string" == typeof r ? r == RSAAPP.NoPadding ? 1 : r == RSAAPP.PKCS1Padding ? 2 : 0 : 0,
    a = "string" == typeof e && e == RSAAPP.RawEncoding ? 1 : 0,
    1 == h ? s > i.chunkSize && (s = i.chunkSize) : 2 == h && s > i.chunkSize - 11 && (s = i.chunkSize - 11),
    t = 0,
    o = 2 == h ? s - 1 : i.chunkSize - 1; s > t; )
        h ? A[o] = n.charCodeAt(t) : A[t] = n.charCodeAt(t),
        t++,
        o--;
    for (1 == h && (t = 0),
    o = i.chunkSize - s % i.chunkSize; o > 0; ) {
        if (2 == h) {
            for (g = Math.floor(256 * Math.random()); !g; )
                g = Math.floor(256 * Math.random());
            A[t] = g
        } else
            A[t] = 0;
        t++,
        o--
    }
    for (2 == h && (A[s] = 0,
    A[i.chunkSize - 2] = 2,
    A[i.chunkSize - 1] = 0),
    S = A.length,
    t = 0; S > t; t += i.chunkSize) {
        for (c = new BigInt,
        o = 0,
        d = t; d < t + i.chunkSize; ++o)
            c.digits[o] = A[d++],
            c.digits[o] += A[d++] << 8;
        P = i.barrett.powMod(c, i.e),
        u = 1 == a ? biToBytes(P) : 16 == i.radix ? biToHex(P) : biToString(P, i.radix),
        f += u
    }
    return f
}
function decryptedString(i, n) {
    var r, e, t, o, d = n.split(" "), h = "";
    for (e = 0; e < d.length; ++e)
        for (o = 16 == i.radix ? biFromHex(d[e]) : biFromString(d[e], i.radix),
        r = i.barrett.powMod(o, i.d),
        t = 0; t <= biHighIndex(r); ++t)
            h += String.fromCharCode(255 & r.digits[t], r.digits[t] >> 8);
    return 0 == h.charCodeAt(h.length - 1) && (h = h.substring(0, h.length - 1)),
    h
}
var RSAAPP = {};
RSAAPP.NoPadding = "NoPadding",
RSAAPP.PKCS1Padding = "PKCS1Padding",
RSAAPP.RawEncoding = "RawEncoding",
RSAAPP.NumericEncoding = "NumericEncoding";
