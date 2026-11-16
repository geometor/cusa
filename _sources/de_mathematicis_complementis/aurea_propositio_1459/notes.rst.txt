:order: 110
:layout: book
:type: notes
:title: Aurea Propositio in Mathematicis — Three-Ray Sum Invariance and the Golden Proposition — Notes
:canonical_id: APM (1459)
:original_id: APM (1459)
:folio: APM (1459)
:tracks: English: index | Latin (1440 / 1514–1913): la | Summary: summary | Notes: notes

.. _aurea_propositio_1459-notes:

====================================================================================================================
Aurea Propositio in Mathematicis — Three-Ray Sum Invariance and the Golden Proposition — Critical Commentary & Notes
====================================================================================================================

.. rubric:: Exact Symbolic Reconstruction, Latin Philology & Canon Reception · APM (1459)

.. picture:: /_static/figures/cusa_aurea_propositio_1459.svg
   :alt: Aurea Propositio in Mathematicis — Three-Ray Sum Invariance and the Golden Proposition
   :caption: Aurea Propositio in Mathematicis (August 8, 1459) — Exact Q(sqrt(3)) Sector (theta = pi/6): Balanced Rectifying Segment I–K–L with |AI| + |AK| + |AL| = 3R and Fifth-Order Maclaurin Residual theta^5/180.

.. picture:: /_static/figures/cusa_aurea_propositio_1459.svg
   :alt: Aurea Propositio in Mathematicis (Rome, August 8, 1459, §§1–7 & Colophon — Complete) — Three-Ray Radial Sum Invariance and the Cusa–Snellius–Huygens Law
   :caption: Aurea Propositio in Mathematicis (1459, §§1–2) — Exact Q(sqrt(3)) Construction at theta = pi/6: Three-Ray Sum |AI| + |AK| + |AL| = 3 Equals Three Unit Radii, with Endpoint Ascent |AI| - 1 = (11 - 6 sqrt(3))/13 Matching Midpoint Descent 1 - |AK| and Fifth-Order Residual theta^5/180.

I. Exact Algebraic Audit of Aurea Propositio in Mathematicis (1459)
-------------------------------------------------------------------

Both *De Mathematica Perfectione* and *Aurea Propositio* converge on the **Cusa–Snellius–Huygens
Law** (:cite:`cusa:perf:1458`, :cite:`cusa:aurea:1459`, :cite:`snellius:huygens:1654`). Let rays
at angles :math:`\pm\theta` (:math:`0 < \theta \le \frac{\pi}{4}`) and central ray :math:`0`
issue from :g:`A` at :math:`(0, 0)` across unit circle :math:`R = 1`, meeting a vertical rectifying
line :math:`x = x_K` at :g:`I`, :g:`K`, :g:`L`, so :math:`|AK| = x_K` and :math:`|AI| = |AL| =
\frac{x_K}{\cos\theta}`. Enforcing Cusa's **Three-Ray Sum Invariance**:

.. math::

   |AI| + |AK| + |AL| = 3 \iff x_K\!\left(1 + \frac{2}{\cos\theta}\right) = 3
   \implies x_K = \frac{3\cos\theta}{2 + \cos\theta}.

At :math:`\theta = \frac{\pi}{6}` (modeled over :math:`\mathbb{Q}(\sqrt{3})` in
``cusa_aurea_propositio_1459.svg``), :math:`x_K = \frac{3\sqrt{3}/2}{2 + \sqrt{3}/2} =
\frac{12\sqrt{3} - 9}{13}`, the outer rays have length :math:`|AI| = |AL| =
\frac{24 - 6\sqrt{3}}{13}`, the combined endpoint ascent :math:`2(|AI| - 1) =
\frac{22 - 12\sqrt{3}}{13}` equals the midpoint descent :math:`1 - x_K`, and the rectified
length is:

.. math::

   L_{\text{Cusa}}(\theta) = 2 x_K \tan\theta = \frac{6\sin\theta}{2 + \cos\theta}
   = 2\theta - \frac{\theta^5}{90} - \frac{\theta^7}{756} - O(\theta^9),

so for the half-arc :math:`\theta - \frac{3\sin\theta}{2 + \cos\theta} =
\frac{\theta^5}{180} + \frac{\theta^7}{1512} + O(\theta^9)`! Because :math:`\cos\theta`
and :math:`\sin\theta` cancel through third order in the `[1/1]` Padé-type rational weight
:math:`\frac{3}{2 + \cos\theta}`, Cusa achieved **fifth-order accuracy**—yielding at
:math:`\theta = \frac{\pi}{6}` an implied :math:`\pi` estimate of
:math:`\frac{18}{2 + \sqrt{3}/2} = \frac{36(4 - \sqrt{3})}{26} \approx 3.140237`, within
:math:`0.043\%` of :math:`\pi`!


IV. Executable Symbolic Verification
------------------------------------

In accordance with GEOMETOR's strict content/code separation for historical editions, executable ``geometor.model`` SymPy constructions, Rational Trigonometry proofs, and series-error audits for **Aurea Propositio in Mathematicis — Three-Ray Sum Invariance and the Golden Proposition** live in ``src/geometor/cusa/`` and the companion walkthrough :doc:`/demos/index`.
