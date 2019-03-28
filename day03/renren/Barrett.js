function BarrettMu(i) {
    this.modulus = biCopy(i),
    this.k = biHighIndex(this.modulus) + 1;
    var t = new BigInt;
    t.digits[2 * this.k] = 1,
    this.mu = biDivide(t, this.modulus),
    this.bkplus1 = new BigInt,
    this.bkplus1.digits[this.k + 1] = 1,
    this.modulo = BarrettMu_modulo,
    this.multiplyMod = BarrettMu_multiplyMod,
    this.powMod = BarrettMu_powMod
}
function BarrettMu_modulo(i) {
    var t = biDivideByRadixPower(i, this.k - 1)
      , u = biMultiply(t, this.mu)
      , o = biDivideByRadixPower(u, this.k + 1)
      , s = biModuloByRadixPower(i, this.k + 1)
      , d = biMultiply(o, this.modulus)
      , r = biModuloByRadixPower(d, this.k + 1)
      , l = biSubtract(s, r);
    l.isNeg && (l = biAdd(l, this.bkplus1));
    for (var h = biCompare(l, this.modulus) >= 0; h; )
        l = biSubtract(l, this.modulus),
        h = biCompare(l, this.modulus) >= 0;
    return l
}
function BarrettMu_multiplyMod(i, t) {
    var u = biMultiply(i, t);
    return this.modulo(u)
}
function BarrettMu_powMod(i, t) {
    var u = new BigInt;
    u.digits[0] = 1;
    for (var o = i, s = t; ; ) {
        if (0 != (1 & s.digits[0]) && (u = this.multiplyMod(u, o)),
        s = biShiftRight(s, 1),
        0 == s.digits[0] && 0 == biHighIndex(s))
            break;
        o = this.multiplyMod(o, o)
    }
    return u
}
