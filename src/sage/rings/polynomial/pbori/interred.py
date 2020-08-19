from .PyPolyBoRi import GroebnerStrategy, Polynomial, ReductionStrategy


def interred(l, completely=False):
    r"""computes a new generating system (g1, ...,gn),
    spanning the same ideal modulo field equations.
    The system is interreduced: For i!=j:
    gi.lead() does not divide any leading term of gj.
    If completely is set to True, then also terms in the
    tail are not reducible by other polynomials.
    """
    l = [Polynomial(p) for p in l if not p == 0]
    if not l:
        return []
    ring = l[0].ring()
    l_old = None
    l = tuple(l)
    while l_old != l:
        l_old = l
        l = sorted(l, key=Polynomial.lead)
        g = ReductionStrategy(ring)
        if completely:
            g.opt_red_tail = True
        for p in l:
            p = g.nf(p)
            if not p.is_zero():
                g.add_generator(p)
        l = tuple([e.p for e in g])
    return list(l)
