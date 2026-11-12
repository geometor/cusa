"""Primary Latin witnesses and original GEOMETOR English translations for Unit V.

Covers:
1. *De Docta Ignorantia* Book II, Chapters 11–12 (1440; Rotta 1913 pp. 113–122),
2. *De Geometricis Transmutationibus* (1445, §§1–11; Paris 1514 vol. II / Basel 1565),
3. *De Mathematicis Complementis* (1453, §§1–10; Paris 1514 vol. II / Basel 1565),
4. *De Mathematica Perfectione* (1458, Ded. & §§1–7; Paris 1514 vol. II / Basel 1565),
5. *Aurea Propositio in Mathematicis* (August 8, 1459, §§1–7 & Colophon, complete).

All English translations are 100% original GEOMETOR scholarly translations rendered
directly from the Latin text.
"""

from __future__ import annotations

from geometor.cusa.texts_u1_u3 import BilingualSectionData

UNIT_5_SECTIONS: tuple[BilingualSectionData, ...] = (
    BilingualSectionData(
        section_id="di-bk2-ch11",
        folio_prefix="DI II.11",
        heading_en="Book II, Chapter 11 — Corollaries Concerning Motion",
        heading_la="Liber II, Capitulum XI — Corollaria de motu",
        witness_note="h I, nn. 156–161 · Paris 1514 fol. 18v–19r · Rotta 1913 pp. 113–116",
        figure_svg=None,
        figure_caption=None,
        la_paragraphs=(
            (
                "DI II.11 §1",
                "Fortassis admirabuntur, qui ista prius inaudita legerint, postquam ea vera esse "
                "docta ignorantia ostendit. Scimus nunc ex istis universum trinum; et nihil "
                "universorum esse, quod non sit unum ex potentia, actu et connexionis motu; et "
                "nullum horum sine alio absolute subsistere posse, ita quod necessario illa in "
                "omnibus sunt secundum diversissimos gradus adeo differenter, quod nulla duo in "
                "universo per omnia aequalia esse possunt simpliciter. Propter quod machinam "
                "mundanam habere aut istam terram sensibilem aut aërem vel ignem vel aliud "
                "quodcumque pro centro fixo et immobili variis motibus orbium consideratis est "
                "impossibile. Non devenitur enim in motu ad minimum simpliciter, puta fixum "
                "centrum, quia minimum cum maximo coincidere necesse est.",
            ),
            (
                "DI II.11 §2",
                "Centrum igitur mundi coincidit cum circumferentia. Non habet igitur mundus "
                "circumferentiam. Nam si centrum haberet, haberet et circumferentiam, et sic intra "
                "se haberet suum initium et finem, et esset ad aliquid aliud ipse mundus "
                "terminatus, et extra mundum esset aliud et locus; quae omnia veritate carent. Cum "
                "igitur non sit possibile mundum claudi intra centrum corporale et "
                "circumferentiam, non intelligitur mundus, cuius centrum et circumferentia sunt "
                "Deus. Et cum non sit mundus infinitus, tamen non potest concipi finitus, cum "
                "terminis careat, intra quos claudatur.",
            ),
            (
                "DI II.11 §3",
                "Terra igitur, quae centrum esse nequit, motu omni carere non potest. Nam eam "
                "moveri taliter etiam necesse est, quod per infinitum minus moveri posset. Sicut "
                "igitur terra non est centrum mundi, ita nec sphaera fixarum stellarum eius "
                "circumferentia, quamvis etiam, comparando terram ad caelum, ipsa terra videatur "
                "centro propinquior et caelum circumferentiae. Non est igitur centrum terra neque "
                "octavae aut alterius sphaerae, neque apparentia super horizontem sex signorum "
                "terram concludit in centro esse octavae sphaerae. Nam si esset etiam distanter a "
                "centro et circa axim per polos transeuntem, ita quod una parte esset elevata "
                "versus unum polum, in alia depressa versus alium, tunc hominibus tantum a polis "
                "distantibus, sicut horizon se extendit, sola medietas sphaerae appareret, ut est "
                "manifestum. Neque etiam est ipsum mundi centrum plus intra terram quam extra, "
                "neque etiam terra ista neque aliqua sphaera habet centrum. Nam cum centrum sit "
                "punctus aequedistans circumferentiae et non sit possibile verissimam sphaeram aut "
                "circulum esse, quin verior dari possit, manifestum est non posse dari centrum, "
                "quin verius etiam dari possit atque praecisius. Aequedistantia praecisa ad "
                "diversa extra Deum reperibilis non est, quia ipse solus est infinita aequalitas. "
                "Qui igitur est centrum mundi, scilicet Deus benedictus, ille est centrum terrae "
                "et omnium sphaerarum atque omnium, quae in mundo sunt; qui est simul omnium "
                "circumferentia infinita.",
            ),
            (
                "DI II.11 §4",
                "Praeterea, non sunt in caelo poli immobiles atque fixi, quamvis etiam caelum "
                "stellarum fixarum videatur per motum describere graduales in magnitudine "
                "circulos, minores quam coluros aut aequinoctialem; et ita de intermediis. Sed "
                "necesse est omnem caeli partem moveri, licet inaequaliter comparatione circulorum "
                "per motum stellarum descriptorum. Unde, sicut quaedam stellae videntur maximum "
                "circulum describere, ita quaedam minimum; sed non reperitur stella, quae nullum "
                "describat. Quoniam igitur non est polus in sphaera fixus, manifestum est neque "
                "aequale medium reperiri quasi aequedistanter a polis. Non est igitur stella in "
                "octava sphaera, quae per revolutionem describat maximum circulum, quoniam illam "
                "aequedistare a polis necesse esset, qui non sunt; et per consequens non est, quae "
                "minimum circulum describat. Poli igitur sphaerarum coincidunt cum centro, ut non "
                "sit aliud centrum quam polus, quia Deus benedictus. Et quoniam nos motum non nisi "
                "comparatione ad fixum, scilicet polos aut centra, deprehendere possumus et illa "
                "in mensuris motuum praesupponimus: hinc in coniecturis ambulantes in omnibus nos "
                "errare comperimus et admiramur, quando secundum regulas antiquorum stellas in "
                "situ non reperimus concordare, quia eos recte de centris et polis et mensuris "
                "credimus concepisse. Ex his quidem manifestum est terram moveri. Et quoniam ex "
                "motu cometae, aëris et ignis elementa experti sumus moveri et lunam minus de "
                "oriente in occasum quam Mercurium aut Venerem vel solem, et ita gradatim: hinc "
                "terra ipsa adhuc minus omnibus movetur, sed tamen non est ut stella circa centrum "
                "aut polum minimum describens circulum; neque octava sphaera describit maximum, ut "
                "statim probatum est.",
            ),
            (
                "DI II.11 §5",
                "Acute igitur considera, quoniam, sicut se habent stellae circa polos "
                "coniecturales in octava sphaera, ita terra, luna et planetae sunt ut stellae "
                "circa polum distanter et differenter motae, coniecturando polum esse, ubi "
                "creditur centrum. Unde, licet terra quasi stella sit propinquior polo centrali, "
                "tamen movetur et non describit minimum circulum in motu, ut est ostensum. Immo "
                "neque sol neque luna neque terra neque aliqua sphaera, licet nobis aliud "
                "videatur, describere potest verum circulum in motu, cum non moveantur super fixo. "
                "Neque verus circulus dabilis est, quin verior dari possit, neque umquam uno "
                "tempore sicut alio aequaliter praecise aut movetur aut circulum verisimilem "
                "aequalem describit, etiamsi nobis hoc non appareat.",
            ),
            (
                "DI II.11 §6",
                "Necesse est igitur, si de motu universi aliquid quoad iam dicta vere intelligere "
                "velis, centrum cum polis complices, te quantum potes cum imaginatione iuvando. "
                "Nam si quis esset supra terram et sub polo arctico et alius in polo arctico, – "
                "sicut existenti in terra appareret polum esse in zenith, ita existenti in polo "
                "appareret centrum esse in zenith. Et sicut antipodes habent sicut nos caelum "
                "sursum, ita existentibus in polis ambobus terra appareret esse in zenith; et "
                "ubicumque quis fuerit, se in centro esse credit. Complica igitur istas diversas "
                "imaginationes, ut sit centrum zenith et e converso, et tunc per intellectum, cui "
                "tantum docta servit ignorantia, vides mundum et eius motum atque figuram attingi "
                "non posse, quoniam apparebit quasi rota in rota et sphaera in sphaera, nullibi "
                "habens centrum vel circumferentiam, ut praefertur.",
            ),
        ),
        en_paragraphs=(
            (
                "DI II.11 §1",
                "Readers who encounter these hitherto unheard-of statements will perhaps marvel, "
                "once learned ignorance demonstrates them to be true. From what has preceded we "
                "now know that the universe is triune; that nothing in the universe exists that is "
                "not one reality formed of potency, act, and the motion of connection; and that "
                "none of these three can subsist absolutely apart from another, so that of "
                "necessity they exist across all things in the most diverse degrees and so "
                "differently that no two things in the universe can be simply equal in every "
                "respect. Consequently, when the varied motions of the orbs are considered, it is "
                "impossible for the fabric of the world to have this sensible earth, or air, or "
                "fire, or anything else whatsoever as a fixed and motionless center. For in motion "
                "one never arrives at an unqualified minimum—such as a fixed center—because the "
                "Minimum must coincide with the Maximum.",
            ),
            (
                "DI II.11 §2",
                "The center of the world, therefore, coincides with its circumference. Hence the "
                "world does not possess a physical circumference. For if it had a center, it would "
                "likewise have a circumference, and thus would contain within itself its own "
                "beginning and end, and the world itself would be bounded against something else, "
                "and outside the world there would be something other and a spatial place—all of "
                "which lack truth. Since, then, the world cannot be enclosed between a bodily "
                "center and a circumference, the world whose center and circumference are God "
                "remains beyond comprehension. And although the world is not infinite, "
                "nevertheless it cannot be conceived as finite, since it lacks bounds within which "
                "it might be enclosed.",
            ),
            (
                "DI II.11 §3",
                "The earth, therefore, which cannot be the center, cannot lack all motion; indeed, "
                "it must move in such a manner that it could always move infinitely less. Just as "
                "the earth is not the center of the world, neither is the sphere of the fixed "
                "stars its circumference, even though when we compare the earth to the heavens the "
                "earth seems nearer to the center and the heavens nearer to the circumference. Nor "
                "is the earth the center either of the eighth sphere or of any other sphere, nor "
                "does the appearance of six zodiacal signs above the horizon prove that the earth "
                "sits at the center of the eighth sphere. For even if the earth stood at some "
                "distance from the center along the axis passing through the poles—raised toward "
                "one pole on one side and lowered toward the other—to observers standing as far "
                "from the poles as the horizon reaches, manifestly half the sphere alone would "
                "still appear. Nor is the center of the world any more inside the earth than "
                "outside it, nor does this earth or any sphere possess a true center. For since a "
                "center is a point equidistant from a circumference and no sphere or circle can "
                "exist so true that a truer could not be given, plainly no center can be given "
                "than which a truer and more exact center could not be given. Precise "
                "equidistance to diverse points is nowhere to be found outside God, because He "
                "alone is infinite equality. He who is the center of the world, namely blessed "
                "God, is therefore the center of the earth, of all spheres, and of all things in "
                "the world, and is simultaneously the infinite circumference of all.",
            ),
            (
                "DI II.11 §4",
                "Furthermore, there are no motionless and fixed poles in the heavens, even though "
                "the heaven of the fixed stars seems by its motion to trace out circles graded in "
                "size, smaller than the colures or the celestial equator, and likewise for "
                "intermediate circles. Rather, every part of the sky must move, albeit unequally "
                "in comparison with the circles traced by the motion of the stars. Thus just as "
                "certain stars seem to trace a largest circle, so others seem to trace a smallest, "
                "yet no star is found that traces none at all. Because no pole in the sphere is "
                "fixed, manifestly no exact middle equidistant from the poles is found either. "
                "Hence there is no star in the eighth sphere that by revolution describes a "
                "strictly maximal circle—since it would have to stand equidistant from poles that "
                "do not exist—and consequently none that describes a strictly minimal circle. The "
                "poles of the spheres therefore coincide with the center, so that the center is no "
                "other than the pole, namely blessed God. And because we can detect motion only by "
                "comparison with something fixed, such as poles or centers, and presuppose these "
                "when measuring motions, walking by conjectures we find that we err in everything, "
                "and we marvel when we discover that the stars do not agree in position according "
                "to the rules of the ancients, because we mistakenly supposed that the ancients "
                "had conceived rightly concerning centers, poles, and measures. From this it is "
                "plain that the earth moves. And since from the motion of a comet we have learned "
                "by experience that the elements of air and fire move, and that the moon moves "
                "less from east to west than Mercury, Venus, or the sun, and so by degrees, the "
                "earth itself moves still less than all the others—yet not like a star describing "
                "a minimal circle around a center or pole, any more than the eighth sphere "
                "describes a maximal circle, as has just been proved.",
            ),
            (
                "DI II.11 §5",
                "Reflect keenly, therefore: just as the stars behave around conjectural poles in "
                "the eighth sphere, so the earth, the moon, and the planets move as stars at "
                "varying distances and speeds around a pole when one conjectures the pole to lie "
                "where the center is believed to be. Hence although the earth, as a star, lies "
                "closer to that central pole, nonetheless it moves and does not describe a minimal "
                "circle in its motion, as has been shown. Indeed, neither the sun nor the moon nor "
                "the earth nor any sphere—though it seem otherwise to us—can trace a true circle "
                "in its motion, since none moves around a fixed point. Neither can a circle be "
                "given without a truer one being possible, nor does any body ever move at one time "
                "with precisely the same equality or trace a like circle equal to that of another "
                "time, even if this is not apparent to us.",
            ),
            (
                "DI II.11 §6",
                "If you wish truly to understand anything of the motion of the universe in light "
                "of what has been said, you must enfold the center together with the poles, aiding "
                "yourself as far as you can with imagination. Suppose one observer stood upon the "
                "earth beneath the arctic pole and another stood at the arctic pole itself: just "
                "as to the observer on earth the pole would appear at the zenith, so to the "
                "observer at the pole the center would appear at the zenith. And just as our "
                "antipodes have the sky overhead even as we do, so to observers at both poles the "
                "earth would appear at the zenith; wherever anyone may be, he believes himself to "
                "stand at the center. Enfold these diverse imaginations together, therefore, so "
                "that the center is the zenith and conversely; then through the intellect—which "
                "learned ignorance alone serves—you behold that the world and its motion and shape "
                "cannot be grasped, for it will appear as a wheel within a wheel and a sphere "
                "within a sphere, having nowhere a center or a circumference, as stated above.",
            ),
        ),
    ),
    BilingualSectionData(
        section_id="di-bk2-ch12",
        folio_prefix="DI II.12",
        heading_en="Book II, Chapter 12 — On the Conditions of the Earth",
        heading_la="Liber II, Capitulum XII — De condicionibus terrae",
        witness_note="h I, nn. 162–174 · Paris 1514 fol. 19r–20v · Rotta 1913 pp. 116–122",
        figure_svg=None,
        figure_caption=None,
        la_paragraphs=(
            (
                "DI II.12 §1",
                "Ad ista iam dicta veteres non attigerunt, quia in docta ignorantia defecerunt. "
                "Iam nobis manifestum est terram istam in veritate moveri, licet nobis hoc non "
                "appareat. Non enim apprehendimus motum nisi per quandam comparationem ad fixum. "
                "Si enim quis ignoraret aquam fluere et ripas non videret existendo in navi in "
                "medio aquae, navem quomodo apprehenderet moveri? Et propter hoc, cum semper "
                "cuilibet videatur, quod sive ipse fuerit in terra sive sole aut alia stella, quod "
                "ipse sit in centro quasi immobili et quod alia omnia moveantur, ille certe semper "
                "alios et alios polos sibi constitueret existens in sole et alios in terra et "
                "alios in luna et Marte, et ita de reliquis. Unde erit machina mundi quasi habens "
                "undique centrum et nullibi circumferentiam, quoniam eius circumferentia et "
                "centrum est Deus, qui est undique et nullibi.",
            ),
            (
                "DI II.12 §2",
                "Terra etiam ista non est sphaerica, ut quidam dixerunt, licet tendat ad "
                "sphaericitatem. Nam figura mundi contracta est in eius partibus, sicut et motus; "
                "quando autem linea infinita consideratur ut contracta taliter, quod ut contracta "
                "perfectior esse nequit atque capacior, tunc est circularis; nam ibi principium "
                "coincidit cum fine. Motus igitur perfectior est circularis, et figura corporalis "
                "perfectior ex hoc sphaerica. Quare omnis motus partis est propter perfectionem ad "
                "totum, ut gravia versus terram et levia sursum, terra ad terram, aqua ad aquam, "
                "aër ad aërem, ignis ad ignem; et motus totius, quantum potest, circularem "
                "concomitatur et omnis figura sphaericam figuram, ut in animalium partibus et "
                "arboribus et caelo experimur. Unde unus motus est circularior et perfectior alio, "
                "ita et figurae sunt differentes.",
            ),
            (
                "DI II.12 §3",
                "Terrae igitur figura est nobilis et sphaerica et eius motus circularis, sed "
                "perfectior esse posset. Et quia maximum aut minimum in perfectionibus, motibus et "
                "figuris in mundo non est, ut ex statim dictis patet, tunc non est verum, quod "
                "terra ista sit vilissima et infima; nam quamvis videatur centralior quoad mundum, "
                "est tamen etiam eadem ratione polo propinquior, ut est dictum. Neque est ipsa "
                "terra pars proportionalis seu aliquota mundi. Nam cum mundus non habeat nec "
                "maximum nec minimum, neque habet medium neque partes aliquotas, sicut nec homo "
                "aut animal; nam manus non est pars aliquota hominis, licet pondus eius ad corpus "
                "videatur proportionem habere; et ita de magnitudine et figura. Neque color "
                "nigredinis est argumentum vilitatis eius; nam in sole si quis esset, non "
                "appareret illa claritas quae nobis. Considerato enim corpore solis, tunc habet "
                "quandam quasi terram centraliorem et quandam luciditatem quasi ignilem "
                "circumferentialem et in medio quasi aqueam nubem et aërem clariorem, quemadmodum "
                "terra ista sua elementa. Unde, si quis foret extra regionem ignis, terra ista in "
                "circumferentia regionis per medium ignis lucida stella appareret, sicut nobis, "
                "qui sumus circa circumferentiam regionis solis, sol lucidissimus apparet. Et non "
                "apparet luna adeo lucida, quoniam forte citra eius circumferentiam sumus versus "
                "partes magis centrales, puta in regione quasi aquea ipsius; et hinc non apparet "
                "eius lumen, licet habeat lumen proprium illis in extremitatibus circumferentiae "
                "eius existentibus apparens, et solum lumen reflexionis solis nobis apparet. Etiam "
                "propterea calor lunae, quem sine dubio ex motu efficit plus in circumferentia, "
                "ubi est maior motus, nobis non communicatur sicut in sole. Unde ista terra inter "
                "regionem solis et lunae videtur situata et per horum medium participat aliarum "
                "stellarum influentiam, quas nos non videmus propter hoc, cum extra earum regiones "
                "simus; videmus enim tantum regiones earum, quae scintillant.",
            ),
            (
                "DI II.12 §4",
                "Est igitur terra stella nobilis, quae lumen et calorem et influentiam habet aliam "
                "et diversam ab omnibus stellis, sicut etiam quaelibet a qualibet lumine, natura "
                "et influentia differt. Et sicut quaelibet stella alteri communicat lumen et "
                "influentiam non ex intentione, quoniam omnes stellae moventur tantum atque "
                "choruscant, ut sint meliori modo, unde ex consequenti participatio oritur, – "
                "sicut lux ex sua natura lucet, non ut ego videam, sed ex consequenti participatio "
                "fit, dum utor lumine ad finem videndi –: ita quidem Deus benedictus omnia "
                "creavit, ut dum quodlibet studet esse suum conservare quasi quoddam munus "
                "divinum, hoc agat in communione cum aliis; ut sicut pes non sibi tantum, sed "
                "oculo et manibus ac corpori et homini toti servit per hoc, quod est tantum ad "
                "ambulandum; et ita de oculo et reliquis membris; pariformiter de mundi partibus. "
                "Plato enim mundum animal dixit; cuius animam absque immersione Deum si concipis, "
                "et multa horum, quae diximus, tibi clara erunt. Neque dici debet, quod quia terra "
                "est minor sole et ab eo recipit influentiam, quod propterea sit vilior; quoniam "
                "regio tota terrae, quae usque ad ignis circumferentiam se extendit, magna est. Et "
                "quamvis terra minor sit quam sol, ut ex umbra et eclipsibus hoc notum nobis est, "
                "tamen non est nobis notum, quantum regio solis sit maior aut minor regione "
                "terrae. Aequalis autem ei praecise esse nequit; nulla enim stella alteri aequalis "
                "esse potest. Neque terra est minima stella, quia est maior luna, ut experientia "
                "eclipsium nos docuit, et Mercurio etiam, ut quidam dicunt, et forte aliis "
                "stellis. Unde ex magnitudine argumentum vilitatem non concludit. Influentia "
                "etiam, quam recipit, non est argumentum concludens imperfectionem. Nam ipsa, ut "
                "est stella, soli et suae regioni forte pariformiter influit, ut praefertur; et "
                "cum non experiamur nos aliter quam in centro esse, in quo confluunt influentiae, "
                "de ista refluentia nihil experiamur. Nam etsi terra quasi possibilitas se habeat "
                "et sol ut anima sive actualitas formalis eius respectu et luna ut medius nexus, "
                "ita ut istae stellae intra unam regionem positae suas ad invicem influentias "
                "uniant, aliis – scilicet Mercurio et Venere et ceteris – supra existentibus, ut "
                "dixerunt antiqui et aliqui etiam moderni: tunc patet correlationem influentiae "
                "talem esse, quod una sine alia esse nequit; erit igitur una et trina in quolibet "
                "pariformiter secundum gradus suos. Quare patet per hominem non esse scibile, an "
                "regio terrae sit in gradu perfectiori et ignobiliori respectu regionum stellarum "
                "aliarum, solis, lunae et reliquarum, quoad ista.",
            ),
            (
                "DI II.12 §5",
                "Neque etiam quoad locum; puta quod hic locus mundi sit habitatio hominum et "
                "animalium atque vegetabilium, quae in gradu sunt ignobiliora in regione solis et "
                "aliarum stellarum habitantium. Nam etsi Deus sit centrum et circumferentia omnium "
                "regionum stellarum et ab ipso diversae nobilitatis naturae procedant in qualibet "
                "regione habitantes, ne tot loca caelorum et stellarum sint vacua et solum ista "
                "terra fortassis de minoribus inhabitata, tamen intellectuali natura, quae hic in "
                "hac terra habitat et in sua regione, non videtur nobilior atque perfectior dari "
                "posse secundum hanc naturam, etiamsi alterius generis inhabitatores sint in aliis "
                "stellis. Non enim appetit homo aliam naturam, sed solum in sua perfectus esse. "
                "Improportionabiles igitur sunt illi aliarum stellarum habitatores, qualescumque "
                "illi fuerint, ad istius mundi incolas, etiamsi tota regio illa ad totam regionem "
                "istam ad finem universi quandam occultam nobis proportionem gerat, ut sic "
                "inhabitatores istius terrae seu regionis ad illos inhabitatores per medium "
                "universalis regionis hinc inde quandam ad se invicem habitudinem gestent, sicut "
                "particulares articuli digitorum manus per medium manus proportionem habent ad "
                "pedem et particulares articuli pedis per medium pedis ad manum, ut omnia ad "
                "animal integrum proportionata sint.",
            ),
            (
                "DI II.12 §6",
                "Unde, cum tota nobis regio illa ignota sit, remanent inhabitatores illi ignoti "
                "penitus, sicut in hac terra accidit, quod animalia unius speciei quasi unam "
                "regionem specificam facientia se uniunt et mutuo propter communem regionem "
                "specificam participant ea, quae eorum regionis sunt, de aliis nihil aut se "
                "impedientes aut veraciter apprehendentes. Non enim animal unius speciei conceptum "
                "alterius, quem per signa exprimit vocalia, apprehendere potest nisi in "
                "paucissimis signis extrinsecus, et tunc per longum usum et solum opinative. Minus "
                "autem de habitatoribus alterius regionis improportionabiliter scire poterimus, "
                "suspicantes in regione solis magis esse solares, claros et illuminatos "
                "intellectuales habitatores, spiritualiores etiam quam in luna, ubi magis "
                "lunatici, et in terra magis materiales et grossi; ut illi intellectuales naturae "
                "solares sint multum in actu et parum in potentia, terrenae vero magis in potentia "
                "et parum in actu, lunares in medio fluctuantes. Hoc quidem opinamur ex influentia "
                "ignili solis et aquatica simul et aërea lunae et gravedine materiali terrae, "
                "consimiliter de aliis stellarum regionibus suspicantes nullam inhabitatoribus "
                "carere, quasi tot sint partes particulares mundiales unius universi, quot sunt "
                "stellae, quarum non est numerus; ut unus mundus universalis sit contractus "
                "triniter progressione sua quaternaria descensiva in tot particularibus, quod "
                "eorum nullus est numerus nisi apud eum, qui omnia in numero creavit. Etiam "
                "corruptio rerum in terra, quam experimur, non est efficax argumentum "
                "ignobilitatis. Nobis enim constare non poterit, postquam est unus mundus "
                "universalis et proportiones influentiales omnium particularium stellarum ad "
                "invicem, quod aliquid sit corruptibile penitus, sed bene secundum alium et alium "
                "essendi modum, quando ipsae influentiae iam quasi contractae in uno individuo "
                "resolvuntur, ut modus essendi sic vel sic pereat, ut non sit morti locus, ut ait "
                "Virgilius. Mors enim nihil esse videtur nisi ut compositum ad componentia "
                "resolvatur; et an talis resolutio solum sit in terrenis incolis, quis scire "
                "poterit?",
            ),
            (
                "DI II.12 §7",
                "Dixerunt quidam tot esse rerum species in terra, quot sunt stellae. Si igitur "
                "terra omnium stellarum influentiam ita ad singulares species contrahit, quare "
                "similiter non fit in regionibus aliarum stellarum influentias aliarum "
                "recipientium? Et quis scire poterit, an omnes influentiae, contractae prius in "
                "compositione, in dissolutione redeant, ut animal nunc existens individuum "
                "alicuius speciei in regione terrae contractum ex omni stellarum influentia "
                "resolvatur, ita ut ad principia redeat, forma tantum ad propriam stellam "
                "redeunte, a qua illa species actuale esse in terra matre recepit? Vel an forma "
                "tantum redeat ad exemplar sive animam mundi – ut dicunt Platonici – et materia ad "
                "possibilitatem, remanente spiritu unionis in motu stellarum, qui spiritus dum "
                "cessat unire, se retrahens ob organorum indispositionem vel alias, ut ex "
                "diversitate motus separationem inducat, tunc quasi ad astra rediens, forma supra "
                "astrorum influentiam ascendente et materia infra descendente? Aut an formae "
                "cuiuslibet regionis in altiori quidem forma, puta intellectuali, quiescant, et "
                "per illam illum finem attingant, qui est finis mundi? Et quomodo hic finis "
                "attingitur per inferiores formas in Deo per illam, et quomodo illa ad "
                "circumferentiam, quae Deus est, ascendat corpore descendente versus centrum, ubi "
                "etiam Deus est, ut omnium motus sit ad Deum; in quo aliquando, sicut centrum et "
                "circumferentia sunt unum in Deo, corpus etiam quamvis visum sit quasi ad centrum "
                "descendere et anima ad circumferentiam, iterum in Deo unientur, cessante non omni "
                "motu, sed eo, qui ad generationem est; tamquam partes illae mundi essentiales "
                "necessario redeant tunc successiva generatione cessante, sine quibus mundus esse "
                "non possit, redeunte etiam spiritu unionis et connectente possibilitatem ad suam "
                "formam.",
            ),
            (
                "DI II.12 §8",
                "Haec quidem nemo hominum ex se, nisi singularius a Deo habuerit, scire poterit. "
                "Licet non dubitet quisquam Deum optimum ad se omnia creasse et non velle quidquam "
                "perire eorum, quae fecit, sciatque eum remuneratorem largissimum omnium ipsum "
                "colentium, modum tamen divinae operationis praesentis et futurae remunerationis "
                "Deus ipse solum scit, qui est sua operatio. Dicam tamen inferius iuxta inspiratam "
                "divinitus veritatem pauca circa hoc, de quibus nunc sufficit in ignorantia "
                "taliter tetigisse.",
            ),
        ),
        en_paragraphs=(
            (
                "DI II.12 §1",
                "To the truths just stated the ancients did not attain, because they fell short in "
                "learned ignorance. To us it is now manifest that this earth in truth moves, even "
                "though this does not appear to us; for we apprehend motion only by some "
                "comparison with a fixed reference. If someone aboard a ship in midstream did not "
                "know that the water was flowing and could not see the banks, how would he perceive "
                "that the ship was moving? For this reason, since to every observer—whether he "
                "stand upon the earth, the sun, or another star—it always seems that he himself "
                "occupies an as-it-were motionless center while all other things move, such an "
                "observer would assuredly set up ever different poles for himself when standing in "
                "the sun, others on the earth, and others on the moon or Mars, and so for all the "
                "rest. Thus the fabric of the world will be as though having its center everywhere "
                "and its circumference nowhere, because its circumference and center are God, who "
                "is everywhere and nowhere.",
            ),
            (
                "DI II.12 §2",
                "Furthermore, this earth is not strictly spherical, as some have claimed, though "
                "it tends toward sphericity. For the shape of the world is contracted in its "
                "parts, just as its motion is; now when the infinite line is considered as "
                "contracted in such a way that as contracted it cannot be more perfect or more "
                "capacious, it is circular, because there the beginning coincides with the end. "
                "The more perfect motion, therefore, is circular, and hence the more perfect "
                "bodily shape is spherical. Accordingly every motion of a part tends toward "
                "perfection in relation to the whole—heavy bodies toward the earth and light ones "
                "upward, earth to earth, water to water, air to air, fire to fire—while the motion "
                "of the whole accompanies circular motion so far as it can, and every shape "
                "accompanies spherical shape, as we experience in the parts of animals, in trees, "
                "and in the heavens. Hence just as one motion is more circular and more perfect "
                "than another, so too shapes differ in degree.",
            ),
            (
                "DI II.12 §3",
                "The shape of the earth, therefore, is noble and spherical and its motion "
                "circular, though it could always be more perfect. Because there is neither a "
                "maximum nor a minimum in perfections, motions, and shapes within the world, as is "
                "plain from what has just been said, it is untrue that this earth is vilest and "
                "lowest; for even if it seems more central with respect to the world, by the very "
                "same reasoning it lies closer to the pole, as already stated. Nor is the earth a "
                "proportional or aliquot part of the world: since the world possesses neither "
                "maximum nor minimum, it possesses neither midpoint nor aliquot parts, any more "
                "than a human being or an animal does—for the hand is not an aliquot fraction of a "
                "human being, even if its weight seems to bear a ratio to the body, and so too for "
                "size and shape. Nor is the earth's dark color proof of baseness; for if someone "
                "stood on the sun, that brightness which appears to us would not appear to him. "
                "When the body of the sun is considered, it possesses a kind of more central "
                "'earth,' a fiery circumferential brilliance, and in between a watery cloud and "
                "clearer air, much as this earth has its own elements. Hence if someone stood "
                "outside the region of fire, our earth would appear as a bright star at the "
                "circumference of its region through the medium of fire, just as to us—situated "
                "around the circumference of the solar region—the sun appears most bright. The "
                "moon does not appear equally bright, perhaps because we stand inside its "
                "circumference toward its more central parts, as it were in its watery region; "
                "thus its own light does not appear to us, though it has proper light visible to "
                "those at the outer rim of its circumference, while to us only the reflected light "
                "of the sun appears. For the same reason the moon's heat, which it doubtless "
                "generates from motion more strongly at its circumference where motion is greater, "
                "is not communicated to us as happens with the sun. Our earth thus seems situated "
                "between the region of the sun and that of the moon, participating through their "
                "medium in the influence of other stars whose bodies we do not see because we lie "
                "outside their regions, seeing only their twinkling outer regions.",
            ),
            (
                "DI II.12 §4",
                "The earth, accordingly, is a noble star possessing light, heat, and influence "
                "distinct and diverse from every other star, just as every star differs from every "
                "other in light, nature, and influence. And just as each star communicates light "
                "and influence to another not by deliberate aim—since all stars move and shine "
                "simply to exist in their best manner, whence participation arises as a "
                "consequence, much as light shines by its own nature rather than in order that I "
                "may see, yet participation follows when I use light for seeing—so blessed God "
                "created all things in such wise that while each strives to conserve its own being "
                "as a divine gift, it does so in communion with all others: just as the foot "
                "serves not itself alone, but eye, hands, body, and the whole human being simply "
                "by existing for walking, and likewise for the eye and remaining members, and in "
                "like manner for the parts of the world. For Plato called the world a living "
                "animal; if you conceive God as its soul without immersion, much of what we have "
                "said will be clear to you. Nor should it be claimed that the earth is baser "
                "because it is smaller than the sun and receives influence from it, since the "
                "entire region of the earth extending out to the circumference of fire is vast; "
                "and although the earth is smaller than the sun, as we know from its shadow and "
                "eclipses, we do not know how much larger or smaller the region of the sun is than "
                "the region of the earth. Precisely equal it cannot be, for no star can equal "
                "another. Nor is the earth the smallest star, since eclipse observations teach us "
                "that it is larger than the moon, and larger than Mercury too as some report, and "
                "perhaps than other stars; size therefore proves no baseness. Neither does "
                "receiving influence prove imperfection: as a star, the earth perhaps exercises a "
                "reciprocal influence upon the sun and its region, though because we experience "
                "ourselves only as standing at a center where influences converge, we sense "
                "nothing of our own outflow. Even if the earth stands as possibility, the sun as "
                "soul or formal actuality in relation to it, and the moon as intermediate bond—so "
                "that these stars placed within one region unite their mutual influences while "
                "Mercury, Venus, and the rest lie beyond, as ancients and some moderns held—plainly "
                "the correlation of influence is such that none can exist without the others, "
                "being at once one and triune in each according to its degree. Plainly, then, no "
                "human being can know whether in these respects the region of the earth stands in "
                "a more perfect or less noble rank than the regions of the sun, moon, and other "
                "stars.",
            ),
            (
                "DI II.12 §5",
                "Nor can this be decided with regard to place—as though this corner of the world "
                "were the dwelling of human beings, animals, and plants lower in rank than those "
                "dwelling in the region of the sun and other stars. For even though God is the "
                "center and circumference of all stellar regions and natures of diverse nobility "
                "proceed from Him to inhabit every region—lest so many expanses of heavens and "
                "stars stand empty while this earth alone, perhaps among the lesser bodies, is "
                "inhabited—nevertheless within the intellectual nature dwelling here on this earth "
                "and in its region it does not appear that anything nobler or more perfect "
                "according to this kind of nature could be given, even if inhabitants of another "
                "genus dwell in other stars. Man does not desire a different nature, but solely to "
                "be perfected within his own. Those inhabitants of other stars, of whatever sort "
                "they may be, thus bear no direct proportion to the dwellers of this world, even "
                "though that whole region bears to this whole region a proportion hidden from us "
                "toward the goal of the universe, so that through the medium of the universal "
                "region the inhabitants here and there stand in mutual relation, just as the "
                "individual joints of the fingers bear a proportion to the foot through the medium "
                "of the hand, and those of the foot to the hand through the foot, so that all are "
                "proportioned to the whole living organism.",
            ),
            (
                "DI II.12 §6",
                "Because that entire region is unknown to us, its inhabitants remain wholly "
                "unknown—just as here on earth animals of a single species, forming as it were one "
                "specific region, unite among themselves and share what belongs to their region "
                "while neither troubling about nor truly grasping the affairs of other species; "
                "for an animal of one species cannot grasp the thought that another expresses by "
                "vocal signs save outwardly in very few signs, after long custom, and merely by "
                "conjecture. Disproportionately less shall we be able to know concerning the "
                "inhabitants of another stellar region, surmising only that in the region of the "
                "sun there dwell more solar, radiant, and illumined intellectual beings, more "
                "spiritual even than in the moon where they are more lunar, while on earth they "
                "are more material and dense—so that solar intellectual natures exist largely in "
                "act and little in potency, earthly ones more in potency and little in act, and "
                "lunar ones fluctuating between. We conjecture this from the fiery influence of "
                "the sun, the watery and airy influence of the moon, and the material heaviness of "
                "the earth, surmising likewise for the other stellar regions that none lacks "
                "inhabitants, as though there were as many particular world-parts of the one "
                "universe as there are stars beyond number, the one universal world being "
                "contracted triply in its fourfold descending progression across particulars "
                "numberless save to Him who created all things in number. Even the corruption of "
                "things experienced on earth is no cogent proof of ignobility: once there is one "
                "universal world and mutual influential proportions among all particular stars, we "
                "cannot be sure that anything perishes utterly rather than merely according to one "
                "or another mode of being when influences contracted in an individual resolve so "
                "that this particular mode ceases—so that, as Virgil says, 'there is no place for "
                "death.' Death seems to be nothing else than a composite resolving into its "
                "components; and who could know whether such resolution occurs among earthly "
                "dwellers alone?",
            ),
            (
                "DI II.12 §7",
                "Some have said that there are as many species of things on earth as there are "
                "stars. If the earth thus contracts the influence of all stars into singular "
                "species, why does the like not happen in the regions of other stars receiving "
                "mutual influences? Who could know whether all influences earlier contracted in "
                "composition return at dissolution, so that a living individual of some species "
                "contracted in the earthly region out of universal stellar influence is resolved "
                "back into its principles, the form alone returning to its proper star whence that "
                "species received actual being in mother earth? Or whether the form returns solely "
                "to the exemplar or World-Soul, as the Platonists hold, and matter to possibility, "
                "while the uniting spirit abides in the motion of the stars—withdrawing on account "
                "of bodily indisposition or other causes so that diversity of motion induces "
                "separation, returning as it were to the stars while form ascends above stellar "
                "influence and matter sinks below? Or whether the forms of every region come to "
                "rest in a higher form, namely the intellectual, and through it attain that goal "
                "which is the goal of the world—ascending through it in God toward the "
                "circumference, which is God, while the body descends toward the center, where God "
                "likewise is, so that the motion of all things tends toward God; in whom one day, "
                "just as center and circumference are one in God, body and soul too, though "
                "seeming to move toward center and circumference respectively, will be reunited in "
                "God when generative motion ceases, the essential parts without which the world "
                "cannot exist returning together as the spirit of union reconnects possibility to "
                "its form?",
            ),
            (
                "DI II.12 §8",
                "Of himself no human being can know these matters unless he has received them by "
                "special gift from God. Though no one doubts that most good God created all things "
                "unto Himself, wills nothing He has made to perish, and is the most bountiful "
                "rewarder of all who revere Him, nevertheless the manner of God's present working "
                "and future reward is known solely to God Himself, who is His own working. Below, "
                "in accordance with divinely inspired truth, I shall say a little more concerning "
                "this, on which it suffices for now to have touched thus in learned ignorance.",
            ),
        ),
    ),
    BilingualSectionData(
        section_id="scripta-geom-trans-1445",
        folio_prefix="DGT",
        heading_en=(
            "De Geometricis Transmutationibus (1445, §§1–11) — To Paolo dal Pozzo "
            "Toscanelli: Isoperimetric Extrema and the Sesquiquartal Radius"
        ),
        heading_la=(
            "De Geometricis Transmutationibus (1445, §§1–11) — Ad Paulum Physicum "
            "Florentinum"
        ),
        witness_note="h XX, Opuscula Mathematica · Paris 1514 vol. II · Basel 1565 pp. 945–949",
        figure_svg="cusa_transmutatio_1445.svg",
        figure_caption=(
            "De Geometricis Transmutationibus (1445, §§9–11) — Inscribed Equilateral Triangle "
            "BCD in Unit Circle A: Quarter-Point E on Side BC Extended in Sesquiquartal Ratio "
            "5:4 Yields Isoperimetric Radius AH = (5/16) sqrt(7), Implying pi ~= (24/35) sqrt(21) "
            "~= 3.142337."
        ),
        la_paragraphs=(
            (
                "DGT §1",
                "Paulo magistri Dominici, physico Florentino, optimo atque doctissimo viro, liber "
                "de geometricis transmutationibus Nicolaus de Cusa cardinalis.",
            ),
            (
                "DGT §2",
                "Etsi veteres magno ingenio praediti sedula indagatione conati sunt multa tunc "
                "abscondita sibi et posteris nota facere perfecerintque utiliter in plerisque "
                "maximis atque optimis artibus, non tamen omne desideratum in quibusque altioribus "
                "theoriis attigerunt, praeordinante hoc universorum optimo provisore, ut in nobis "
                "vis illa divinae intelligentiae non torpeat, sed admiratione vehementiori ad ipsa "
                "latentia et scitu possibilia feratur. Ardentius quidem in obscuri penetrationem "
                "movemur, ut quietius de mentis vigorositate delectemur. Inter ea autem, quae "
                "geometricis speculationibus insudantibus hucusque impedimento fuere, unum ab "
                "omnibus, quorum vires ingenii libri, qui ad nostram notitiam deducti sunt, "
                "curiosius observant, incognitum remansit, de recti scilicet atque curvi "
                "aequalitate aut in invicem transmutatione statuenda, ita ut non minimis, immo "
                "paene omnibus huic inquisitioni deditis post immensos labores visum sit viam ad "
                "huius notitiam acquirendam a nobis sublatam, hoc rei impossibilitate agente et "
                "natura ipsam tantae oppositionis coincidentiam repellente. Ego vero rei huius "
                "difficultatem in parvitate apprehensionis et intermissione diligentiae, non summo "
                "acumine vigilantium, ut obscuritas negotii deposcit, potius existimans dato "
                "qualicumque otio ad artem novam, qua ad quaesitum pertingerem, me contuli ei "
                "diligenter satis ob altiores fines insudando, quousque cunctarum meditationum "
                "mearum subscriptam formula facilem resolutionem efficerem. Quoniam autem in tanta "
                "et hactenus ignota arte, a qua non tantum perfectio geometricae transmutationis "
                "dependet, sed et etiam introductio ad altiora ascendendi figuratur, non erat in "
                "obscuritate et parvitate ingenioli mei confidendum, recte statui ad te, arbitrum "
                "peritissimum atque veritatis zelatorem, confugere et iamdudum probatissimo amico "
                "inventionem pandere, ut in statera aequissimi iudicis aestimetur. Noli igitur, "
                "amice dilectissime, ista, etiam si in maioribus verseris, quasi cruda "
                "indigestaque abicere. Lectu enim parva, intellectu vero facillima sunt. Sed "
                "quanto me ab annis iuventutis atque adolescentiae nostrae strictiori amicitiae "
                "nodo atque cordiali quodam amplexu indesinenter constrinxisti, tanto nunc "
                "accuratius emendationi animum adhibe et in communionem aliorum nisi correctum "
                "prodire non sinas.",
            ),
            (
                "DGT §3",
                "Post innumeros paene modos, quibus, semper tamen deficiens, ad institutam artem "
                "pervenire contendi, tandem ad principium, quo in De docta ignorantia usus sum, "
                "respiciens via mihi patefacta existit. Exigit autem ars, quam inquiro, praeter ea "
                "iam tradita in geometricis versionem curvi in rectum ac recti in curvum. Inter "
                "quae cum nulla rationalis proportio cadat, oportet in quadam coincidentia "
                "extremorum hoc latere secretum. Quae cum in maximo sit, ut alibi traditur, et "
                "maximum sit circulus, qui ignoratur, in minimo, qui est triangulus, inquiri ipsum "
                "debere ibi ostenditur.",
            ),
            (
                "DGT §4",
                "Omnium autem figurarum multorum angulorum, quae polygoniae, et aequalium laterum, "
                "quae isopleurae, et eiusdem longitudinis laterum, quae eandem habentes "
                "peripheriam isoperimetrae dicuntur, triangularem minimae capacitatis existere "
                "constat. Et cum tanto quaelibet isoperimetra sit capacior, quanto plures angulos "
                "habuerit, erit circulus isoperimeter figurarum omnium capacissima. Ad quam per "
                "angulorum multiplicationem deveniri nequit, sicut nec in numero ad maximum. Nulla "
                "igitur polygonia ad circularem isoperimetram proportionem rationalem habere "
                "potest.",
            ),
            (
                "DGT §5",
                "Quia vero differentia capacitatis isoperimetrarum figurarum correspondet "
                "differentiae semidiametrorum circulorum inscriptorum eisdem, ut iam ante hoc "
                "notum est, quare nec circulus inscriptus, qui semper minor est, nec "
                "circumscriptus, qui semper maior est, ad circulum isoperimetrum rationalem "
                "proportionem habebit. Semidiametri autem illorum iam dictorum circulorum maxime "
                "inaequales in trigono existunt, in aliis successive minus inaequales, in circulo "
                "vero isoperimetro coincidentes, cum ibi inscriptus, circumscriptus et peripheria "
                "coincidant. Hinc inquirendum, qua arte ad coincidentiam ipsam atque propositum "
                "nostrum pertingere valeamus.",
            ),
            (
                "DGT §6",
                "Videtur autem ad artis quaesitae sufficientiam primum pertinere, ut datae rectae "
                "detur aequalis curva. Secundo, ut secundum habitudinem curvae ad curvam detur "
                "recta ad rectam. Tertio, ut inter datas lineas duae proportionales assignentur. "
                "Quarto, ut secundum habitudinem duarum datarum sciatur ad tertiam datam dari "
                "quarta. Primum hactenus ignotum. Secundum nondum consideratum. Tertium a paucis "
                "obscure tactum. Quartum clare a multis explicatum. Complicatur in his omne, quod "
                "transmutatoriae huic arti opportunum est, ut praemissis istis, quae circa haec "
                "necessaria sunt, in exemplaribus subsumptionibus ostendere conabor.",
            ),
            (
                "DGT §7",
                "Posse lineam curvam esse, quae datae rectae nec maior nec minor sit, ab omnibus "
                "admittitur, licet non omnes eam signari posse affirment. Potest igitur "
                "peripheriae datae polygoniae circuli alicuius peripheria nec maior nec minor "
                "esse, ut sint isoperimetrae. Sed quomodo haec detur, inquirimus.",
            ),
            (
                "DGT §8",
                "Quoniam autem tanto circulus polygoniae aequilaterae seu isopleurae "
                "circumscriptus maior est quanto ipsa paucorum angulorum, et ei inscriptus tanto "
                "minor, hinc nemo negare potest, quin omnis circulus polygoniae aequilaterae "
                "inscriptus minor sit circulo isoperimetro atque quod omnis circumscriptus maior. "
                "Quare inter inscriptum atque circumscriptum isoperimeter cadens habet "
                "semidiametrum omni semidiametro cuiuscumque inscripti circuli cuicumque "
                "polygoniae isopleurae et isoperimetrae maiorem et circumscripti semidiametro "
                "minorem. Manifestabitur autem id, quod quaerimus, post multos difficiliores modos "
                "facili consequentia ex hac propositione:",
            ),
            (
                "DGT §9",
                "Semidiameter circuli isoperimetri trigono inscripto se habet ad lineam a centro "
                "circuli, cui trigonus inscribitur, ad quartam lateris ductam in proportione "
                "sesquiquarta.",
            ),
            (
                "DGT §10",
                "Sit circulus super a centro descriptus, cui bcd trigonus inscribitur, diviso bc "
                "latere in quattuor partes aequales per e, f, g signatas. Dico, si de a ad e linea "
                "ducta extendatur per quartam sui, ut sit ah, illam fore semidiametrum circuli, "
                "cuius circumferentia aequatur tribus trigoni lateribus.",
            ),
            (
                "DGT §11",
                "Hoc sic facillime verum comprobatur. Nam tracta de a ad f linea illam "
                "semidiametrum circuli inscripti fore constat, quae est omnium inscriptorum "
                "polygoniis isoperimetris minima. Et similiter linea de a ad b ducta est "
                "semidiameter circumscripti, quae est omnium circumscriptorum isoperimetris "
                "polygoniis maxima. Et si de a prope f ad i punctum lineam duxeris extendendam "
                "secundum habitudinem if portionis ad bc latus, quae extensa sit ak, illam minorem "
                "esse semidiametro circuli isoperimetri manifestum, cum semidiameter circuli "
                "isoperimetri sit omnium inscriptorum polygoniis isoperimetris maxima. Similiter "
                "si de a prope b ad punctum l linea ducta extensa fuerit secundum habitudinem "
                "portionis lf ad bc, quae sit am, illam esse maiorem quaesita per se clarum est, "
                "cum quaesita sit omnium semidiametrorum circulorum circumscriptorum polygoniis "
                "isoperimetris minima. Potest igitur inter l et i ad aliquem punctum de a linea "
                "duci, quae extensa secundum habitudinem portionis inter punctum illum et f "
                "cadentis ad latus bc aequabitur quaesitae.",
            ),
        ),
        en_paragraphs=(
            (
                "DGT §1",
                "To Paolo, son of Master Domenico, Florentine physician, most excellent and "
                "learned man: the book On Geometric Transmutations of Nicholas of Cusa, Cardinal.",
            ),
            (
                "DGT §2",
                "Although the ancients, endowed with great genius, strove by diligent inquiry to "
                "make known to themselves and posterity many truths then hidden and achieved "
                "fruitful mastery across most of the greatest and best arts, still they did not "
                "attain everything desired in every loftier theory—the supreme Provider of the "
                "universe having foreordained this lest the power of divine intelligence within us "
                "grow sluggish, rather than being borne by keener wonder toward things hidden yet "
                "accessible to knowledge. Indeed we are stirred all the more ardently to penetrate "
                "what is obscure so that we may delight more serenely in the vigor of the mind. "
                "Now among the obstacles that have hitherto hindered those sweating over geometric "
                "speculations, one problem has remained unknown to all whose intellectual powers "
                "are recorded in the books brought to our notice: namely, establishing the "
                "equality or mutual transmutation of the straight and the curved—so much so that "
                "to nearly all who have devoted themselves to this quest after immense labors it "
                "has seemed that the road to acquiring knowledge of it is barred to us, the "
                "impossibility of the thing causing this and nature itself repelling the "
                "coincidence of so great an opposition. Judging, however, that the difficulty of "
                "this matter lay rather in narrowness of apprehension and slackening of diligence "
                "among investigators not watching with the sharpest acumen demanded by the "
                "obscurity of the task, whenever any leisure was granted me I betook myself to a "
                "new art whereby I might reach what was sought, laboring over it quite diligently "
                "for the sake of higher ends until I reduced all my meditations to an easy "
                "resolution by the formula written below. Yet because in an art so great and "
                "hitherto unknown—on which depends not only the perfection of geometric "
                "transmutation, but in which an introduction for ascending to higher realities is "
                "also figured—I ought not to trust the obscurity and smallness of my slender wit, "
                "I rightly resolved to turn to you, a most skilled judge and lover of truth, and "
                "lay open my discovery to a long-tested friend to be weighed in the balance of a "
                "most impartial arbiter. Do not cast these pages aside as crude and undigested, "
                "dearest friend, even if you are occupied with greater affairs; they are brief to "
                "read and very easy to understand. Rather, in proportion as since the years of our "
                "youth and adolescence you have unceasingly bound me in the closest knot of "
                "friendship and heartfelt embrace, apply your mind all the more carefully now to "
                "correcting this work, and suffer it not to go forth into common hands unless "
                "emended.",
            ),
            (
                "DGT §3",
                "After nearly countless attempts by which, ever falling short, I strove to reach "
                "the proposed art, at last when I looked back to the principle I employed in On "
                "Learned Ignorance a pathway opened before me. Beyond what has already been handed "
                "down in geometry, the art I seek requires turning the curved into the straight "
                "and the straight into the curved. Since no rational proportion falls between "
                "these two, this secret must lie hidden in a certain coincidence of extremes. And "
                "since that coincidence resides in the maximum, as explained elsewhere, and the "
                "maximum here is the circle which is unknown, it is shown there that it must be "
                "sought within the minimum, which is the triangle.",
            ),
            (
                "DGT §4",
                "Among all many-angled figures (called polygons) having equal sides (called "
                "equilateral or isopleural) and equal total perimeter (called isoperimetric), it "
                "is established that the triangular figure possesses minimal area-capacity. And "
                "since every isoperimetric polygon is the more capacious the more angles it "
                "possesses, the isoperimetric circle will be the most capacious of all figures. "
                "Yet one cannot arrive at that circle by multiplying angles, any more than one "
                "arrives at a maximum in number. No polygon, therefore, can bear a rational "
                "proportion to the isoperimetric circle.",
            ),
            (
                "DGT §5",
                "Because the difference in area-capacity among isoperimetric figures corresponds "
                "to the difference among the radii of the circles inscribed in them, as is already "
                "known, neither the inscribed circle (which is always smaller) nor the "
                "circumscribed circle (which is always larger) will bear a rational proportion to "
                "the isoperimetric circle. Now the radii of those inscribed and circumscribed "
                "circles are maximally unequal in the triangle, successively less unequal in "
                "higher polygons, and coincident in the isoperimetric circle itself, where "
                "incircle, circumcircle, and perimeter coincide. Hence we must inquire by what art "
                "we may attain that coincidence and our goal.",
            ),
            (
                "DGT §6",
                "Four tasks appear sufficient for the art we seek: first, given a straight line, "
                "to exhibit an equal curve; second, according to the ratio of curve to curve, to "
                "exhibit straight line to straight line; third, between given lines to assign two "
                "mean proportionals; fourth, according to the ratio of two given lines, for a "
                "third given line to exhibit a fourth proportional. The first has hitherto been "
                "unknown; the second not yet considered; the third touched upon darkly by a few; "
                "the fourth clearly explained by many. Within these four is enfolded everything "
                "needful for this transmutatory art, as I shall endeavor to show in exemplary "
                "applications once the necessary preliminaries are set down.",
            ),
            (
                "DGT §7",
                "Everyone admits that there can exist a curved line neither greater nor smaller "
                "than a given straight line, even if not everyone affirms that it can be "
                "constructed. The circumference of some circle can therefore be neither greater "
                "nor smaller than the perimeter of a given polygon, so that the two are "
                "isoperimetric; how such a circle may be exhibited is what we investigate.",
            ),
            (
                "DGT §8",
                "Because the circumscribed circle of an equilateral polygon is all the larger the "
                "fewer angles the polygon has, while its inscribed circle is all the smaller, no "
                "one can deny that every circle inscribed in an equilateral polygon is smaller "
                "than the isoperimetric circle and every circumscribed circle is larger. Falling "
                "between the incircle and the circumcircle, therefore, the isoperimetric circle "
                "has a radius greater than every inradius and smaller than every circumradius of "
                "any equilateral polygon of the same perimeter. After many harder methods, what we "
                "seek will become manifest by easy consequence from the following proposition:",
            ),
            (
                "DGT §9",
                "Proposition: The radius of the circle isoperimetric to an inscribed equilateral "
                "triangle stands to the line drawn from the center of the circumscribing circle to "
                "the quarter-point of a side in the sesquiquartal ratio [5 : 4].",
            ),
            (
                "DGT §10",
                "Let a circle be described about center a with an equilateral triangle bcd "
                "inscribed in it, and let side bc be divided into four equal parts marked by e, f, "
                "g. I say that if the line drawn from a to e is produced by one-fourth of itself "
                "so as to become ah, then ah will be the radius of the circle whose circumference "
                "equals the three sides of the triangle.",
            ),
            (
                "DGT §11",
                "This is verified very easily as follows. Drawing the line from a to midpoint f, "
                "plainly af is the radius of the inscribed circle, which is the smallest among all "
                "incircles of isoperimetric polygons; similarly the line drawn from a to vertex b "
                "is the radius of the circumscribed circle, which is the largest among all "
                "circumcircles of isoperimetric polygons. If from a you draw a line to a point i "
                "very near f and extend it in the ratio of segment if to side bc, producing ak, "
                "manifestly ak is smaller than the radius of the isoperimetric circle, since the "
                "isoperimetric radius exceeds every inradius. Likewise if from a you draw a line "
                "to a point l near b and extend it in the ratio of segment lf to bc, producing am, "
                "clearly am is larger than the sought radius, since the sought radius is smaller "
                "than every circumradius. Between l and i, therefore, a line can be drawn from a "
                "to some intermediate point which, extended according to the ratio of the segment "
                "between that point and f to side bc, will equal the radius sought.",
            ),
        ),
    ),
    BilingualSectionData(
        section_id="scripta-math-compl-1453",
        folio_prefix="DMC",
        heading_en=(
            "De Mathematicis Complementis (1453, §§1–10) — To Pope Nicholas V: "
            "Archimedes' Spiral and the Convergence of Inradius and Circumradius"
        ),
        heading_la="De Mathematicis Complementis (1453, §§1–10) — Ad Nicolaum Papam Quintum",
        witness_note="h XX, Opuscula Mathematica · Paris 1514 vol. II · Basel 1565 pp. 1005–1010",
        figure_svg=None,
        figure_caption=None,
        la_paragraphs=(
            (
                "DMC §1",
                "Tanta est potestas summi tui pontificatus, Nicolae quinte, pater beatissime, ut "
                "per eos, qui vim eius attente consideraverunt, assimiletur potentiae quadrandi "
                "rotundum et quadrum circulandi, quasi maior illi dari non possit. Verum, cum in "
                "te non tantum primatus sit clavis et potestas scientiae supremaeque hierarchiae "
                "ecclesiae, sed velut perfectus magister omnium scibilium ex tuo felicissimo "
                "ingenio incomparabilis notitiae esse iudiceris ab omnibus. Id magnificentissime "
                "effecisti, ut omnium tam Graecorum quam Latinorum scripta, quae reperiri queunt, "
                "tua mirifica diligentia in omnium nostrum notitiam accuratissime pervenerint, "
                "ita, ut etiam geometrica non neglexeris, quae sane omni honore digna a maioribus "
                "nostris habita fuerunt.",
            ),
            (
                "DMC §2",
                "Tradidisti etenim mihi proximis diebus magni Archimedis geometrica Graece tibi "
                "praesentata et tuo studio in Latinum conversa, quae mihi tam admiranda visa sunt, "
                "ut circa ipsa non nisi magna cum diligentia versari potuissem. Ex quo id effectum "
                "est, ut meo studio et labore complementum aliquod illis addiderim, quod tuae "
                "sanctitati offerre decrevi. Solum enim te dignum scio, ut quae a saeculo "
                "incognita remanserunt, per te cunctis patescant. Et non tantum scibilia, quae "
                "semper circa quaesitam circuli quadraturam versari consueverunt, sed et quae in "
                "omni mathematica perfectione praestant complementum, ex his ipsis meo iudicio "
                "perfecte consequi possint.",
            ),
            (
                "DMC §3",
                "Testimonio omnium, qui se ad geometrica contulerunt, nemo propinquius Archimede "
                "ad circuli pervenit quadraturam. Qui videns illam attingi non posse, nisi curva "
                "circularis linea in rectam resolvatur, nisus est hanc artem mediante helica "
                "ostendere. Sed quia proportio motus signi a centro per semidiametrum ad motum, in "
                "quo in eodem tempore aliud signum per circumferentiam movetur, sine qua helica "
                "describi nequit, se habet ut semidiameter ad circumferentiam, quae non est scita, "
                "sed quaeritur. Hinc videtur ipsum defecisse. Facilius enim erit circulum quadrare "
                "quam helicam describere et contingentem eidem in fine circulationis applicare. "
                "Remanet igitur ex his, quae Archimedes reliquit, haec ars adhuc penitus "
                "abscondita. Ego autem quamvis multos in vanum laborasse in hac legerim "
                "indagatione, temptare coepi, si forte haec difficultas possit medio "
                "coincidentiarum finem capere, uti in aliis scientiis vim illam maximam esse "
                "comperi. Et visum est mihi quod data possibilitate, quam passim omnes admittunt, "
                "faciliter possit huius scientia pariter et praxis modo, quo sequitur, adipisci.",
            ),
            (
                "DMC §4",
                "Primo advertendum quod in figura multiangula seu polygonia, quae habet aequalia "
                "latera, punctus unus aequedistans a medio et fine laterum centrum dicitur et "
                "linea ab illo centro ducta ad medium lateris est semidiameter circuli inscripti "
                "eidem et vocetur prima linea. Et alia linea ducta ab eodem centro ad finem "
                "lateris seu angulum aliquem est semidiameter circuli circumscripti eidem et "
                "vocetur secunda linea. Hae duae lineae in omni multiangula diversae sunt "
                "quantitatis et tanto plus, quanto latus eius maius. Nam potentia secundae lineae "
                "continet potentiam primae et cum hoc potentiam medietatis lateris, quia latus "
                "trianguli orthogonii, quod opponitur angulo recto, ut ostendit Euclides.",
            ),
            (
                "DMC §5",
                "Et quia prima figurarum rectilinearum est triangulus, hinc in eo differunt in "
                "quantitate prima et secunda lineae maxime. In circulo vero coincidunt, quia ibi "
                "centrum aequaliter distat a circumferentia; medium enim et finis lateris "
                "coincidunt et est undique angulus. Est autem prima linea in trigono brevissima et "
                "secunda longissima. In eiusdem peripheriae tetragono prima post primam trigoni "
                "brevissima et sic secunda post secundam trigoni longissima et ita consequenter. "
                "Et quoniam prima in tetragono tali longior est prima in trigono, si ducitur prima "
                "in tetragono in medietatem peripheriae et similiter prima in trigono in eandem "
                "medietatem, diversas superficies, quae aequantur polygoniis, oriri constat.",
            ),
            (
                "DMC §6",
                "Unde excessus superficiei illius, quae ex prima tetragoni ducta in medietatem "
                "peripheriae, super superficiem, quae oritur ex ductu primae trigoni in eandem "
                "medietatem peripheriae, est excessus capacitatis tetragoni super capacitatem "
                "trigoni, et sic quidem in cunctis polygoniis ex excessu primae lineae cuiuslibet "
                "super primam trigoni isoperimetri deprehenditur excessus capacitatis ipsius "
                "polygoniae super capacitatem trigoni. Quanto autem differentia primae et secundae "
                "linearum est minor, tanto excessus primae lineae polygoniae super primam trigoni "
                "maior. Et quia in circulo coincidunt prima et secunda, excessus semidiametri "
                "circuli isoperimetri super primam trigoni est maximus et hinc circuli capacitas "
                "super capacitatem trigoni maxima. Unde linea una recta, quae in trigono ad tria "
                "latera est extensa, ut sit illius superficiei perimeter, in tetragono ad quattuor "
                "latera extenditur, ut sit tetragoni perimeter, et adhuc plus in pentagono. Si "
                "autem maxime extenditur, ita quod plus extendi non possit, erit perimeter "
                "circuli.",
            ),
            (
                "DMC §7",
                "Ex his patet, quod si trigonus est minimae capacitatis, ubi prima et secunda "
                "lineae maxime differunt, et circulus maximae capacitatis, ubi prima et secunda "
                "lineae coincidunt, erit sic proportionabiliter in mediis polygoniis. Quare, si "
                "ponitur excessus capacitatis circuli super trigonum, ut est differentia primae et "
                "secundae lineae in trigono, erit excessus capacitatis circuli super tetragonum ut "
                "differentia primae et secundae lineae in tetragono et ita consequenter, cum ad "
                "maiorem excessum primae lineae unius super primam lineam alterius sequatur minor "
                "differentia primae et secundae in excedente quam sit primae et secundae in "
                "excessa. Ex quo faciliter dato excessu primae in una aliqua super primam trigoni "
                "et differentia differentiarum primae et secundae illius capacioris et primae et "
                "secundae trigoni potest haberi semidiameter circuli isoperimetri, cuius scilicet "
                "circumferentia aequatur tribus lateribus trigoni aut quattuor tetragoni.",
            ),
            (
                "DMC §8",
                "Quo scito patet circuli quadratura. Nam si ducitur semidiameter illius circuli "
                "isoperimetri in medietatem peripheriae, oritur superficies quadrangularis, quae "
                "nec maior nec minor esse potest superficie circulari, ut Archimedes faciliter "
                "ostendit. Haec superficies quadrangularis in quadratam ducitur, quoniam costa "
                "eius erit medium proportionale inter semidiametrum circuli et semiperipheriam "
                "eius, quae ex nona sexti Euclidis invenitur. Omnia haec quamvis manifesta sint, "
                "volo tamen illa etiam illis, qui mathematicis operam non impenderunt, clarissima "
                "facere. Figurae autem multiangulae similium laterum et aequalium peripheriarum, "
                "de quibus loquar, polygoniae isopleures et isoperimetrae ex conformitate Graecae "
                "linguae apud aliquos reperiuntur nominari.",
            ),
            (
                "DMC §9",
                "Si ducitur linea recta in lineam rectam, oritur figura quattuor rectorum "
                "angulorum, et si eadem ducitur in duplam, oritur dupla, et ita deinceps. Et si "
                "recta ducitur de angulo in angulum, diameter est, quia in duo dividit. Ut si ab "
                "linea ducitur in bc, oritur figura quadrangularis abcd habens quattuor angulos "
                "rectos. Et si ab ducitur in be, quae sit dupla ad bc, oritur quadrangulus abef, "
                "qui est duplus ad abcd. Linea vero ac diameter est, similiter et ae.",
            ),
            (
                "DMC §10",
                "Multiplicatio primae lineae in medietatem peripheriae aequatur embado polygoniae. "
                "Sit abcd figura quadrata quattuor rectorum angulorum et aequalium laterum. Cui "
                "inscribatur circulus super e centro, ita quod tangat quattuor latera quadrati in "
                "medio, et trahatur de e ad contactum, ubi circulus tangit ab, linea ef, quae est "
                "prima, quia semidiameter inscripti, et trahatur eb linea et similiter de e ad "
                "contactum, ubi circulus bd latus tangit, et sit eg, et dupletur linea fb, et sit "
                "fh, et similiter dupletur eg, et sit ei dupla, et claudatur quadrangulus per "
                "lineam ih, et ducatur eh diameter. Manifestum est ex praemissa efb et ebh "
                "triangulos esse aequales. Primus enim est medietas primi quadranguli, quia eb "
                "diameter, et efh triangulus est medietas secundi quadranguli, qui est duplus ad "
                "primum, quia eh diameter.",
            ),
        ),
        en_paragraphs=(
            (
                "DMC §1",
                "So great is the authority of your supreme pontificate, most blessed Father "
                "Nicholas V, that by those who have attentively pondered its force it is likened "
                "to the power of squaring the round and rounding the square, as though none "
                "greater could be bestowed upon it. In you resides not only the primacy of the "
                "keys and authority over learning and the supreme hierarchy of the Church, but by "
                "universal judgment you are esteemed from your most happy genius to be like a "
                "consummate master of incomparable knowledge across all knowable things. Most "
                "magnificently have you brought it about that through your marvellous diligence "
                "all discoverable writings of Greeks and Latins alike have come with utmost "
                "accuracy to the knowledge of us all—not neglecting even geometric treatises, "
                "which by our forebears were rightly held worthy of every honor.",
            ),
            (
                "DMC §2",
                "Indeed in recent days you placed in my hands the geometric works of great "
                "Archimedes, presented to you in Greek and translated into Latin through your "
                "zeal, which struck me as so admirable that I could study them only with the "
                "greatest diligence. As a result, through my study and toil I have added to them a "
                "certain mathematical complement which I have resolved to offer to Your Holiness; "
                "for I know you alone to be worthy that truths remaining unknown for ages should "
                "through you be laid open to all. In my judgment not only the problems customarily "
                "revolving around the long-sought quadrature of the circle, but also those that "
                "supply completion across all mathematical perfection, can be attained from these "
                "principles.",
            ),
            (
                "DMC §3",
                "By the testimony of all who have devoted themselves to geometry, no one came "
                "closer to squaring the circle than Archimedes. Seeing that this cannot be "
                "attained unless the curved circular line is resolved into a straight line, he "
                "strove to demonstrate this art by means of the spiral. Yet because the ratio of "
                "the motion of a point moving from the center along the radius to the motion by "
                "which in the same time another point travels along the circumference—without "
                "which the spiral cannot be described—is the very ratio of radius to "
                "circumference, which is not known but is the thing sought, on this point he "
                "appears to have fallen short; for it will prove easier to square the circle than "
                "to trace the spiral and apply a tangent to it at the end of a revolution. From "
                "what Archimedes left behind, therefore, this art still remains deeply hidden. "
                "Although I had read that many labored in vain over this inquiry, I began to test "
                "whether this difficulty might reach completion through the medium of "
                "coincidences, whose power I had found supreme in other sciences; and granting the "
                "possibility universally admitted, it seemed to me that both the theory and the "
                "practice of this art can readily be won in the manner that follows.",
            ),
            (
                "DMC §4",
                "First let it be noted that in an equilateral many-angled or polygonal figure the "
                "single point equidistant from the midpoints and endpoints of the sides is called "
                "the center; the line drawn from that center to the midpoint of a side is the "
                "radius of the inscribed circle, and let it be called the 'first line' [inradius]. "
                "The other line drawn from the same center to the endpoint of a side, that is, to "
                "a vertex angle, is the radius of the circumscribed circle, and let it be called "
                "the 'second line' [circumradius]. In every polygon these two lines differ in "
                "magnitude, and all the more so the longer its side; for the square on the second "
                "line contains the square on the first line together with the square on half the "
                "side, being the side opposite the right angle in a right triangle, as Euclid "
                "demonstrates.",
            ),
            (
                "DMC §5",
                "Because the triangle is the first of rectilinear figures, in it the first and "
                "second lines differ maximally in magnitude. In the circle, by contrast, they "
                "coincide, since there the center stands equidistant from the circumference—the "
                "midpoint and endpoint of the side coinciding where every point is angle. In the "
                "equilateral triangle the first line is shortest and the second line longest; in "
                "the square of the same perimeter the first line is next shortest after that of "
                "the triangle and the second line next longest, and so onward in succession. "
                "Because the first line in such a square exceeds the first line in the triangle, "
                "multiplying each first line by half the common perimeter manifestly produces "
                "distinct rectangular areas equal to the respective polygons.",
            ),
            (
                "DMC §6",
                "Consequently the excess of the area formed from the square's first line "
                "multiplied by the semiperimeter over the area formed from the triangle's first "
                "line multiplied by the same semiperimeter equals the excess of the square's "
                "capacity over the triangle's capacity; and in every polygon the excess of its "
                "first line over the first line of the isoperimetric triangle measures the excess "
                "of its capacity over the triangle's. Now the smaller the difference between first "
                "and second lines, the greater the excess of that polygon's first line over the "
                "triangle's first line; and because in the circle first and second lines coincide, "
                "the excess of the isoperimetric circle's radius over the triangle's first line is "
                "maximal, and hence the circle's capacity exceeds the triangle's maximally. Thus a "
                "single straight line bent around three sides as a triangle's perimeter, then "
                "around four sides as a square's, and still further in a pentagon, when extended "
                "maximally so that it can be extended no further, becomes the circumference of a "
                "circle.",
            ),
            (
                "DMC §7",
                "From this it is clear that if the triangle has minimal capacity where first and "
                "second lines differ maximally, and the circle has maximal capacity where first "
                "and second lines coincide, intermediate polygons behave proportionally. Setting "
                "the excess of the circle's capacity over the triangle's proportional to the "
                "difference between first and second lines in the triangle, and its excess over "
                "the square's proportional to their difference in the square, from the excess of "
                "any higher polygon's first line over the triangle's together with the difference "
                "of their radial gaps one seeks the radius of the isoperimetric circle whose "
                "circumference equals the three sides of the triangle or the four sides of the "
                "square.",
            ),
            (
                "DMC §8",
                "Once that radius is known, the quadrature of the circle is plain: multiplying the "
                "radius of that isoperimetric circle by half its perimeter yields a rectangular "
                "area neither greater nor smaller than the circular area, as Archimedes easily "
                "demonstrated; and this rectangle is converted into a square whose side is the "
                "mean proportional between the radius and the semiperimeter, found from Book VI "
                "of Euclid. Though all these steps are familiar to geometers, I wish to render "
                "them crystal clear even to readers unpracticed in mathematics. Such equilateral "
                "many-angled figures of equal perimeter are called in Greek fashion 'isopleural "
                "and isoperimetric polygons.'",
            ),
            (
                "DMC §9",
                "Multiplying a straight line by a straight line produces a figure of four right "
                "angles; multiplying the same line by double the length produces double the "
                "rectangle, and so on; and a straight line drawn from corner to opposite corner is "
                "the diagonal because it bisects the figure. Thus ab multiplied by bc produces "
                "rectangle abcd of four right angles, and ab multiplied by be (double bc) produces "
                "rectangle abef, double abcd, with diagonals ac and ae.",
            ),
            (
                "DMC §10",
                "Theorem: Multiplying the first line [inradius] by half the perimeter equals the "
                "area of the regular polygon. Let abcd be a square of four right angles and equal "
                "sides, with a circle inscribed about center e touching the four sides at their "
                "midpoints. Draw ef to the point of contact on ab—this is the first line, being "
                "the inradius—and draw vertex ray eb and contact radius eg to side bd; double fb "
                "to fh, double eg to ei, close the rectangle with ih, and draw diagonal eh. From "
                "the preceding lemma triangles efb and ebh are equal, so triangle efh is half the "
                "doubled rectangle, proving that the inradius multiplied by the semiperimeter "
                "equals the polygon's area.",
            ),
        ),
    ),
    BilingualSectionData(
        section_id="scripta-math-perf-1458",
        folio_prefix="DMP",
        heading_en=(
            "De Mathematica Perfectione (1458, Ded. & §§1–7) — To Cardinal Antonio "
            "Cerdà: Intellectual Vision of Vanishing Sagitta and the 3 : (2 + cos θ) Law"
        ),
        heading_la=(
            "De Mathematica Perfectione (1458, Ded. & §§1–7) — Ad Dominum Antonium "
            "Cardinalem Sancti Chrysogoni"
        ),
        witness_note="h XX, Opuscula Mathematica · Paris 1514 vol. II · Basel 1565 pp. 1110–1114",
        figure_svg=None,
        figure_caption=None,
        la_paragraphs=(
            (
                "DMP Ded.",
                "Reverendissimo in Christo Patri, domino Antonio sanctae Romanae ecclesiae tituli "
                "sancti Chrysogoni presbytero cardinali, Nicolaus cardinalis tituli sancti Petri "
                "ad vincula de mathematica perfectione.",
            ),
            (
                "DMP §1",
                "Sollicita est nobilis mens vestra, Pater reverendissime, ut videat etiam "
                "hebetiorum speculationes, et a me alias novi aliquid deposcebat. Et quoniam me a "
                "palatio pes morbidus excusavit, biduo domi sedens mathematicam perfectionem, quam "
                "mitto, conscripsi, quatenus virtutem coincidentiarum experimento ignotorum "
                "hactenus in theologicis inquisitionibus commendarem. Omne enim scibile "
                "mathematicum ex ipsa, uti exempla quaedam subiungo, attingitur in his obscuris "
                "semper quam avide quaesitis, quae nulli hactenus patuerunt. Quomodo autem "
                "mathematica nos ducant ad penitus absoluta divina et aeterna, melius me novit "
                "doctissima paternitas vestra, qui estis theologorum vertex. Quandam etiam meae "
                "considerationis circa speculum et aenigma parvam alligavi scripturam: ubi si "
                "Reverendissima Paternitas Vestra modicum versari dignabitur, subito videbit, si "
                "visum mentis recte in rerum conieci principium, haec talia, quae etiam a "
                "doctissimis scribi timebantur. Quoniam minus apte panduntur quam contemplentur, "
                "non erubui Paternitati Vestrae mittere, cuius iudicio dirigi opto, sciens me non "
                "alieno, sed patri, qui me amat, communicare secreta, quae mihi pretiosiora "
                "fortassis videntur quam existant: correcturus aestimationem secundum vestram "
                "sententiam, quam istis libellis supplex ascribi deposco.",
            ),
            (
                "DMP §2",
                "Intentio est ex oppositorum coincidentia mathematicam venari perfectionem. Et "
                "quia perfectio illa plerumque consistit in rectae curvaeque quantitatis "
                "adaequatione, propono habitudinem duarum rectarum linearum se ut chorda ad suum "
                "arcum habentium investigare, sciens illa habita me medium habere curvam "
                "quantitatem cum recta adaequandi; et quoniam ad has inveniendas necesse est me "
                "alicuius chordae ad arcum habitudinem scire, ut ex illa cognita pergere queam ad "
                "artem. Sed quomodo est possibile me cuiusquam datae chordae ad arcum habitudinem "
                "scire, cum inter illas quantitates adeo contrarias forte non cadat numerabilis "
                "habitudo?",
            ),
            (
                "DMP §3",
                "Necesse erit igitur me recurrere ad visum intellectualem, qui videt minimam, sed "
                "non assignabilem chordam cum minimo arcu coincidere. Nam quanto chorda minor, "
                "tanto sagitta adhuc minor, ut de sagitta chordae bc est minor quam ge sagitta "
                "chordae fh, quia bc minor fh, et ita consequenter.",
            ),
            (
                "DMP §4",
                "Minima igitur chorda, qua minor dari non posset, si signabilis foret, non haberet "
                "sagittam, et ita etiam non foret minor arcu suo. Coincideret igitur ibi chorda et "
                "arcus, si ad minimam quantitatem in talibus deveniretur. Hoc videt bene "
                "intellectus necessarium, licet sciat nec arcum nec chordam, cum sint quantitates, "
                "esse simpliciter minimas in actu et posse, cum continuum sit semper divisibile. Ad "
                "hauriendum autem scientiam habitudinis respicio ad intellectualem visionem et "
                "dico me videre, ubi est chordae et arcus aequalitas, scilicet in simpliciter "
                "minimo utriusque. Ex hac visa aequalitate pergo ad inquirendum intentum medio "
                "trianguli orthogonii, et hoc per propositionem, quae sequitur.",
            ),
            (
                "DMP §5",
                "Si orthogonii latus, quo non est maius, ponitur linea prima et semidiameter "
                "circuli, et latus, quo non est minus, secunda linea et semichorda, et reliquum "
                "latus tertia linea: quae erit semiarcus ad semichordam habitudo, illa erit lineae "
                "aequalis tribus primis lineis ad lineam aequalem duabus primis cum tertia. Ut si "
                "orthogonius est abc et ac latus, quo non est maius, prima linea et semidiameter "
                "circuli, et bc latus, quo non est minus, secunda linea et semichorda, et ab latus "
                "tertia linea, et hc semiarcus, et de aequalis tribus lineis ac, et fg aequalis "
                "duabus ac cum una ab. Dico, quod quae est habitudo hc ad bc illa est de ad fg.",
            ),
            (
                "DMP §6",
                "Orthogonius est tanto minor, quanto prima linea tertiam minus excedit. Si igitur "
                "posset dari minimus orthogonius, prima tertiam non excederet, et quia secunda "
                "linea foret minima, tunc cum ponatur semichorda, ipsa non foret minor semiarcu "
                "secundum praemissa. Maximus autem orthogonius est, quando prima tertiam excedit "
                "maxime. Et hoc erit, quando tertia erit ut secunda, qua non est minor, et tunc "
                "secunda est semichorda quadrantis. Et sit ille orthogonius abc. Dico possibile "
                "esse, quod aliqua linea addatur ac et eadem addatur ab, et maior se habeat ad "
                "minorem ut hc semiarcus ad bc semichordam. Hanc lineam posse dari, quae addatur "
                "ac et ab, ut praefertur, certum relinquo, cum possit linea aliqua dari, quae "
                "addita ad ac et ab efficiat lineas maioris habitudinis quam est habitudo hc "
                "semiarcus ad bc, et possit dari linea, quae addita efficiat lineas minoris "
                "habitudinis quam hc ad bc, et hoc certum. Igitur et dari posse eam, quae addita "
                "efficiat lineas nec maioris nec minoris habitudinis quam hc ad bc, manifestum, "
                "cum non repugnet lineas rectas se habere ut chorda ad arcum, sive chorda sit "
                "arcui commensurabilis sive incommensurabilis.",
            ),
            (
                "DMP §7",
                "Constat autem, quod qualiscumque illa linea fuerit, si in minimo orthogonio etiam "
                "ad ac et ab additur, propositio verificatur, cum ibi prima et tertia sic sint "
                "eadem sicut semiarcus et semichorda. Quare qualiscumque illa linea fuerit, quae "
                "additur, propositio vera manet. Et quia sic est, quod linea, quae additur in "
                "maximo orthogonio, est etiam illa, quae additur in minimo, igitur et in omnibus "
                "orthogoniis intermediis eadem manebit.",
            ),
        ),
        en_paragraphs=(
            (
                "DMP Ded.",
                "To the Most Reverend Father in Christ, Lord Antonio, Cardinal Priest of the Holy "
                "Roman Church of the title of Saint Chrysogonus: Nicholas, Cardinal of the title "
                "of Saint Peter in Chains, On Mathematical Perfection.",
            ),
            (
                "DMP §1",
                "Your noble mind is solicitous, Most Reverend Father, to examine even the "
                "speculations of duller wits, and on an earlier occasion asked me for something "
                "new. Excused from the papal palace by a gouty foot and sitting at home for two "
                "days, I composed On Mathematical Perfection, which I send herewith in order to "
                "commend for theological inquiries the power of coincidences through an empirical "
                "trial upon mathematical problems hitherto unknown. For every knowable truth in "
                "mathematics, as I illustrate by certain examples subjoined here, is attained from "
                "that coincidence across obscure questions ever eagerly sought yet hitherto patent "
                "to none. How mathematics leads us to wholly absolute, divine, and eternal "
                "realities Your most learned Paternity—who stand at the summit of theologians—"
                "knows far better than I. I have also enclosed a brief writing of my reflections "
                "concerning the mirror and the enigma [De Beryllo], wherein if Your Most Reverend "
                "Paternity deigns to linger a little, you will straightway see whether I have "
                "rightly cast the gaze of the mind into the principle of things—matters that even "
                "the most learned shrank from committing to writing. Because such things are set "
                "forth less aptly than they are contemplated, I have not blushed to send them to "
                "Your Paternity, by whose judgment I wish to be guided, knowing that I impart not "
                "to a stranger but to a father who loves me secrets that perhaps seem more "
                "precious to me than they really are, ready to correct my estimate according to "
                "your verdict, which as a suppliant I beg you to inscribe upon these little books.",
            ),
            (
                "DMP §2",
                "My aim is to hunt down mathematical perfection out of the coincidence of "
                "opposites. Because that perfection consists chiefly in equating straight and "
                "curved quantity, I propose to investigate the ratio of two straight lines "
                "standing to one another as a chord stands to its arc, knowing that once this "
                "ratio is in hand I possess the medium for equating curved quantity with straight. "
                "Yet since to discover these lines I must know the ratio of some chord to its arc "
                "so as to advance from it to the art, how is it possible for me to know the ratio "
                "of any given chord to its arc when between quantities so contrary no numerable "
                "ratio may fall?",
            ),
            (
                "DMP §3",
                "I must therefore have recourse to intellectual vision, which beholds that the "
                "minimal—though unassignable—chord coincides with the minimal arc. For the smaller "
                "the chord, the smaller still is its sagitta: thus the sagitta de of chord bc is "
                "smaller than the sagitta ge of chord fh because bc is smaller than fh, and so "
                "onward in succession.",
            ),
            (
                "DMP §4",
                "The minimal chord, therefore, than which none smaller could be given, if it could "
                "be marked out, would have zero sagitta and so would not be shorter than its arc; "
                "chord and arc would coincide there if one arrived at minimal quantity in such "
                "things. The intellect sees clearly that this is necessary, even while knowing "
                "that neither arc nor chord, being continuous magnitudes, can be unqualifiedly "
                "minimal in act or potency, since the continuum is endlessly divisible. Yet to "
                "draw forth knowledge of their ratio I look to intellectual vision and affirm that "
                "I behold where the equality of chord and arc resides: namely, in the unqualified "
                "minimum of both. From this beheld equality I proceed to seek my goal by means of "
                "a right triangle, through the proposition that follows.",
            ),
            (
                "DMP §5",
                "Proposition: In a right triangle, let the greatest side [hypotenuse] be called "
                "the first line and serve as radius of a circle, let the least side [opposite leg] "
                "be called the second line and serve as half-chord, and let the remaining side "
                "[adjacent leg] be called the third line: then as the half-arc stands to the half-"
                "chord, so stands a line equal to three first lines to a line equal to two first "
                "lines together with one third line. That is, in right triangle abc with "
                "hypotenuse ac as first line and radius, opposite leg bc as second line and half-"
                "chord, adjacent leg ab as third line, hc as half-arc, de equal to three times ac, "
                "and fg equal to twice ac plus ab, I say that as hc stands to bc, so de stands to "
                "fg [namely θ / sin θ ≈ 3 / (2 + cos θ)].",
            ),
            (
                "DMP §6",
                "A right triangle is all the smaller the less its first line exceeds its third "
                "line. Were a minimal right triangle given, the first line would not exceed the "
                "third, and since the second line would be minimal, serving as half-chord it would "
                "not be smaller than the half-arc, as shown above. The largest symmetric right "
                "triangle here considered occurs when the third line equals the second line, so "
                "that the second line is the half-chord of a quadrant [θ = π/4]. I affirm that "
                "some single line can be added alike to ac and to ab such that the larger sum "
                "stands to the smaller sum as half-arc hc stands to half-chord bc: for since one "
                "added line yields a greater ratio than hc : bc and another yields a lesser ratio, "
                "plainly a line can be given yielding a ratio neither greater nor lesser than hc : "
                "bc, whether chord and arc be commensurable or incommensurable.",
            ),
            (
                "DMP §7",
                "Now whatever that added line may be, when it is likewise added to ac and ab in "
                "the minimal right triangle the proportion holds automatically, because there "
                "first and third lines coincide just as half-arc and half-chord coincide [at θ -> "
                "0, (R + c)/(R cos θ + c) -> 1, and matching curvature fixes c = 2R]. Treating the "
                "line added in the maximal triangle as identical to that in the minimal triangle, "
                "we apply the same law across all intermediate right triangles.",
            ),
        ),
    ),
    BilingualSectionData(
        section_id="scripta-aurea-prop-1459",
        folio_prefix="APM",
        heading_en=(
            "Aurea Propositio in Mathematicis (Rome, August 8, 1459, §§1–7 & Colophon — "
            "Complete) — Three-Ray Radial Sum Invariance and the Cusa–Snellius–Huygens Law"
        ),
        heading_la=(
            "Aurea Propositio in Mathematicis (Romae, VIII. Augusti 1459, §§1–7 — "
            "Textus Integer)"
        ),
        witness_note="h XX, Opuscula Mathematica · Basel 1565 pp. 1145–1146",
        figure_svg="cusa_aurea_propositio_1459.svg",
        figure_caption=(
            "Aurea Propositio in Mathematicis (1459, §§1–2) — Exact Q(sqrt(3)) Construction at "
            "theta = pi/6: Three-Ray Sum |AI| + |AK| + |AL| = 3 Equals Three Unit Radii, with "
            "Endpoint Ascent |AI| - 1 = (11 - 6 sqrt(3))/13 Matching Midpoint Descent 1 - |AK| "
            "and Fifth-Order Residual theta^5/180."
        ),
        la_paragraphs=(
            (
                "APM §1a",
                "Sive tres lineae a centro egressae angulos aequales semirectos aut minores "
                "constituentes per arcum seu chordam terminentur, eandem ad terminantem tenent "
                "habitudinem.",
            ),
            (
                "APM §1b",
                "Uti si de a, centro bdc, indefinitae quantitatis lineae egrediantur, duos "
                "aequales circa a angulos semirectos seu minores constituentes, per alicuius "
                "circuli arcum, puta bdc, aut eius chordam, scilicet bhc, sive contingentem, puta "
                "edg, terminentur: eandem teneant tres lineae ab, ad et ac ad arcum terminantem "
                "habitudinem quam ab, ah et ac ad bhc terminantem, sive ae, ad et ag ad edg "
                "terminantem. Quod idem est ac si diceretur: Sicut bdc arcus est quadrans et tres "
                "lineae ab, ad et ac sunt tres semidiametri eius, sic edg est aequalis alicui "
                "quadranti et ae, ad et ag aequantur tribus semidiametris circuli eius.",
            ),
            (
                "APM §2",
                "Ratio huius, quoniam si arcus bdc deberet in rectam, cuius extrema aequedistant "
                "ab a centro, inter lineas de a per b et de a per c egredientes cadentem extendi, "
                "necesse foret extrema cum medio simul tam rectae quam arcus aequedistare ab a "
                "centro. Si enim extrema aequedistarent, tunc medium rectae minus distaret quam "
                "medium arcus ab a centro, et recta foret minor arcu, ut in chorda bhc. Et si "
                "media aequedistarent, tunc extrema rectae plus distarent ut in contingente edg, "
                "ideo ipsa maior arcu bdc. Oportet igitur, quod quantum medium arcus, dum "
                "extenditur, descendit ad centrum, quod tantum extrema ascendant a centro, ut in "
                "ikl, ubi medium arcus in extensione de d descendit in k, et b et c extrema "
                "ascendunt in i et l; et extremorum ascensus aequatur descensui medii, ita quod "
                "extrema cum medio rectae simul aequedistant ab a centro, sicut extrema simul cum "
                "medio bdc arcus. Unde si non foret aequedistantia talis, recta non aequaretur "
                "illi arcui, sed simili maioris circuli, si maior distantia a centro, vel minori, "
                "si minor.",
            ),
            (
                "APM §3",
                "Et quia, quanto circulus maior est, tanto arcus rectae similior, ideo videt mens, "
                "si infinite maximus circulus signabilis foret, arcum esse et rectam et haec, quae "
                "dicta sunt ibi atque propositionem veram. Et quoniam stante eodem angulo circa "
                "centrum eadem est habitudo terminantium et terminatarum, ideo id, quod in maximo "
                "videt mens verum, in omnibus pariformiter verum esse conspicit. Propositio igitur "
                "illis et aliis innumeris modis verissima conspicitur.",
            ),
            (
                "APM §4",
                "Ratio, cur propositio de duobus semirectis, qui rectum angulum faciunt, et "
                "minoribus et non universaliter de omnibus angulis loquitur, haec est, quia a "
                "minimo arcu et portione circuli usque ad quadrantem triangulus ex orthogoniis "
                "compositus et portioni circuli inscriptus continue augetur et fit maximus in "
                "quadrante, post minuitur. Et ideo non potest propositio aeque vera esse arcu cum "
                "portione et triangulo crescente atque arcu cum portione crescente et triangulo "
                "decrescente.",
            ),
            (
                "APM §5",
                "Patet faciliter omnem arcum rectilineari posse. Nam si tres lineae in recta "
                "terminatae sunt pars aliquota trium semidiametrorum, recta talis erit aliquota "
                "arcus, curva tamen superficies est capacior recta. Sic si tertiam partem trium "
                "terminatarum in recta sumpseris et semidiametrum feceris describendo arcum, ille "
                "rectae aequabitur, et universaliter arcum in rectam et rectam in arcum vertes et "
                "arcum unius circuli in arcum alterius.",
            ),
            (
                "APM §6",
                "Constat etiam, quod anguli dari possunt, qui se habent ut costa et diameter "
                "quadrati et universaliter sicut dabiles lineae, ita et superficies et corpora. "
                "Habes etiam innumerabiles modos circulum rectilineandi, quadrangulandi et "
                "quadrandi. Sic de qualibet portione circuli commensurabili circulo vel "
                "incommensurabili. Patescunt etiam ignota de sinibus et chordis. Haec omnia "
                "hactenus in mathematicis incognita et quaeque mathematice scibilia cum infinitis "
                "inauditis corollariis ad hoc datis quaerentes reperient.",
            ),
            (
                "APM §7",
                "Altius se elevantes vident aequalitatem habitudinis esse medium transmutationis "
                "atque transitus de contrario in contrarium, et quid mysterii habet, quod tres "
                "lineae a puncto egredientes aut terminantur in uno arcu, et sunt omnes aequales, "
                "aut in recta, et extremae sunt aequales et media inaequalis usque ad "
                "incommensurabilitatem, sicut costa est et diameter quadrati. Et diversitas "
                "terminationis diversificat superficies, ut una sit curva, alia recta, manente "
                "eadem habitudine terminantium, quae linearum ex eodem puncto et modo aequali "
                "egredientium. Nec hoc citra nec ultra trinitatem linearum, quae non ut separatae, "
                "sed ut una simplex longitudo considerantur, verum esse potest. Circa unitrinum "
                "igitur principium et rerum ab eo effluxum versabitur altissima sapientis "
                "speculatio.",
            ),
            (
                "APM Col.",
                "Finit Romae 1459, 8. Augusti, tempore legationis urbis etc.",
            ),
        ),
        en_paragraphs=(
            (
                "APM §1a",
                "Golden Proposition: Whether three lines issuing from a center and forming two "
                "equal half-right [45°] or smaller angles are terminated by a circular arc or by "
                "a straight chord, the sum of the three rays bears the same ratio to the "
                "terminating line.",
            ),
            (
                "APM §1b",
                "Specifically, let lines of indefinite length issue from a, the center of arc bdc, "
                "forming two equal half-right or smaller angles around a, and let them be "
                "terminated either by the arc of some circle, say bdc, or by its chord bhc, or by "
                "its tangent edg: then the three lines ab, ad, and ac hold the same ratio to the "
                "terminating arc bdc as ab, ah, and ac hold to the terminating chord bhc, or as "
                "ae, ad, and ag hold to the terminating tangent edg. Which is the same as saying: "
                "just as when arc bdc is a quadrant and the three lines ab, ad, and ac are three "
                "of its radii, so edg equals the quadrant of another circle whose three radii "
                "taken together equal ae, ad, and ag.",
            ),
            (
                "APM §2",
                "The reason is this: if the arc bdc is to be straightened out into a rectifying "
                "segment falling between the outer rays through b and c whose endpoints stand "
                "equidistant from center a, its two endpoints taken together with its midpoint "
                "must have the same total distance from center a as the endpoints and midpoint of "
                "the arc. For if the endpoints alone kept the same distance, the midpoint of the "
                "straight segment would lie closer to center a than the midpoint of the arc, and "
                "the segment would be shorter than the arc, as in chord bhc; whereas if the "
                "midpoints kept the same distance, the endpoints of the straight segment would "
                "lie farther out, as in tangent edg, which is therefore longer than arc bdc. As "
                "the arc is straightened out into ikl, therefore, however much its midpoint "
                "descends toward the center from d to k, by that combined amount its endpoints b "
                "and c must ascend outward from the center to i and l—so that the ascent of the "
                "endpoints balances the descent of the midpoint [AI + AK + AL = 3R], "
                "keeping endpoints plus midpoint collectively equidistant from center a just like "
                "the arc bdc. Without such collective equidistance the segment would equal not "
                "that arc, but a similar arc of a larger or smaller circle.",
            ),
            (
                "APM §3",
                "Because the larger the circle is, the more closely its arc resembles a straight "
                "line, the mind sees that if an infinitely maximal circle could be marked out, arc "
                "and straight line would coincide and everything just stated—and the proposition "
                "itself—would hold exactly. And since while the central angle remains fixed the "
                "ratio of terminating lines to terminated rays stays invariant across circles of "
                "every size, what the mind beholds to be true in the Maximum it beholds to hold "
                "likewise across finite circles.",
            ),
            (
                "APM §4",
                "The reason why the proposition speaks of two half-right angles (making one right "
                "angle) or smaller angles rather than universally of all angles is this: from the "
                "minimal arc and circular sector up to the quadrant [2θ = 90°], the inscribed "
                "isosceles triangle composed of two right triangles [area R² sin θ cos θ = ½ R² "
                "sin 2θ] continually increases and reaches its maximum at the quadrant, after "
                "which it diminishes. Hence the proposition cannot hold in the same way both when "
                "arc, sector, and triangle grow together and when arc and sector grow while the "
                "triangle shrinks.",
            ),
            (
                "APM §5",
                "Plainly, then, any arc within this range can readily be rectified: if the sum of "
                "the three rays terminated on a straight segment is an aliquot part of three "
                "radii, that straight segment will be the same part of the arc, though the curved "
                "sector remains more capacious in area than the rectilinear triangle. Taking one-"
                "third of the sum of the three rays terminated on a given straight segment as "
                "radius and describing an arc between the outer rays, that arc will equal the "
                "straight segment; universally you will convert arc into straight line, straight "
                "line into arc, and an arc of one circle into an arc of another.",
            ),
            (
                "APM §6",
                "It is likewise established that angles can be exhibited standing to one another "
                "as the side and diagonal of a square, and universally as any constructible lines, "
                "surfaces, and solids; you possess countless ways of rectifying, rectangularizing, "
                "and squaring the circle and any commensurable or incommensurable circular sector, "
                "and hitherto unknown properties of sines and chords become plain.",
            ),
            (
                "APM §7",
                "Those who raise their minds higher behold that equality of ratio is the medium of "
                "transmutation and of passage from contrary into contrary, and behold what mystery "
                "resides in the fact that three lines issuing from a single point either terminate "
                "upon a single circular arc—where all three are equal—or terminate upon a straight "
                "line—where the two outer rays are equal and the middle ray is unequal even unto "
                "incommensurability, like the side and diagonal of a square. Diversity of "
                "termination diversifies the enclosed surfaces, rendering one curved and the other "
                "rectilinear while preserving the selfsame ratio between terminating boundaries "
                "and the rays issuing symmetrically from the same point. Neither short of nor "
                "beyond a trinity of lines—considered not as severed pieces, but as one simple "
                "length—can this hold true. Around the Unitrine Principle and the outflow of all "
                "things from it, therefore, will revolve the loftiest speculation of the wise.",
            ),
            (
                "APM Col.",
                "Finished at Rome, August 8, 1459, during the legation of the City, etc.",
            ),
        ),
    ),
)
