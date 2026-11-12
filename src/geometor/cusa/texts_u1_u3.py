"""Primary Latin witnesses and original GEOMETOR English translations for Units I–III.

All Latin texts derive from public-domain witnesses:

- Paolo Rotta, *Nicolai Cusani De docta ignorantia libri tres* (Bari: Laterza, 1913),
  verified by multimodal scan inspection against Raymond Klibansky's annotated copy
  (McGill University Library) and the Renaissance *editiones principes* of Jacques
  Lefèvre d'Étaples (Paris, 1514) and Heinrich Petri (Basel, 1565), restoring Rotta's
  two homeoteleuton omissions in Book I, Chapters 13 and 14.

All English translations in this module are 100% original GEOMETOR scholarly translations
rendered directly from the Latin text.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BilingualSectionData:
    """Synchronized Latin and original English paragraphs for one treatise section."""

    section_id: str
    folio_prefix: str
    heading_en: str
    heading_la: str
    witness_note: str
    figure_svg: str | None
    figure_caption: str | None
    la_paragraphs: tuple[tuple[str, str], ...]
    en_paragraphs: tuple[tuple[str, str], ...]


UNIT_1_SECTIONS: tuple[BilingualSectionData, ...] = (
    BilingualSectionData(
        section_id="di-dedicatio",
        folio_prefix="DI Ded.",
        heading_en="Dedicatory Prologue to Cardinal Julian Cesarini",
        heading_la="Dedicatio ad Dominum Iulianum Cardinalem",
        witness_note="h I, n. 1 · Paris 1514 fol. 1r · Rotta 1913 p. 1",
        figure_svg=None,
        figure_caption=None,
        la_paragraphs=(
            (
                "DI Ded. §1",
                "Deo amabili reverendissimo patri domino Iuliano sanctae Apostolicae Sedis "
                "dignissimo cardinali, praeceptori suo metuendo.",
            ),
            (
                "DI Ded. §2",
                "Admirabitur et recte maximum tuum et iam probatissimum ingenium, quid sibi hoc "
                "velit, quod, dum meas barbaras ineptias incautius pandere attempto, te arbitrum "
                "eligo, quasi tibi pro tuo cardinalatus officio apud Apostolicam Sedem in publicis "
                "maximis negotiis occupatissimo aliquid otii supersit et post omnium Latinorum "
                "scriptorum, qui hactenus claruerunt, supremam notitiam et nunc Graecorum etiam ad "
                "meum istum fortassis ineptissimum conceptum tituli novitate trahi possis, qui "
                "tibi, qualis ingenio sim, iam dudum notissimus existo. Sed haec admiratio, non "
                "quod prius incognitum hic insertum putes, sed potius qua audacia ad de docta "
                "ignorantia tractandum ductus sim, animum tuum sciendi peravidum spero visendum "
                "alliciet. Ferunt enim naturales appetitum quandam tristem sensationem in stomachi "
                "orificio anteire, ut sic natura, quae se ipsam conservare nititur, stimulata "
                "reficiatur. Ita recte puto admirari, propter quod philosophari, sciendi desiderium "
                "praevenire, ut intellectus, cuius intelligere est esse, studio veritatis "
                "perficiatur. Rara quidem, etsi monstra sint, nos movere solent. Quamobrem, "
                "praeceptorum unice, pro tua humanitate aliquid digni hic latitare existimes, et "
                "ex Germano in rebus divinis talem qualem ratiocinandi modum suscipe, quem mihi "
                "labor ingens admodum gratissimum fecit.",
            ),
        ),
        en_paragraphs=(
            (
                "DI Ded. §1",
                "To his revered teacher, the father beloved of God and most reverend Lord Julian, "
                "most worthy Cardinal of the Holy Apostolic See.",
            ),
            (
                "DI Ded. §2",
                "Your supreme and long-tested intellect will rightly wonder what I intend when, "
                "venturing somewhat incautiously to lay bare my unpolished awkwardnesses, I choose "
                "you as judge—as though any leisure remained to you amid the gravest public "
                "affairs of your cardinalatial office at the Apostolic See, and as though, after "
                "mastering the highest knowledge of all Latin writers who have hitherto shone "
                "forth and now of the Greeks as well, you could be drawn by the novelty of a title "
                "toward this perhaps clumsy conception of mine, when you have long known full well "
                "what measure of mind I possess. Yet I hope that this very wonder—not because you "
                "suppose anything hitherto unknown is set down here, but rather out of curiosity "
                "at the boldness by which I have been led to treat of learned ignorance—will "
                "entice your mind, ever eager for knowledge, to look within. Natural philosophers "
                "report that a certain sharp pang at the mouth of the stomach precedes appetite, "
                "so that nature, striving to preserve itself, may be aroused and restored. In just "
                "this way I judge that wonder, on account of which philosophy begins, runs ahead "
                "of the desire to know, so that the intellect, whose very being is to understand, "
                "may be brought to perfection through the study of truth. Uncommon things, even "
                "when monstrous, are wont to stir us. Therefore, matchless teacher, deem in your "
                "kindness that something of worth lies hidden here, and receive from a German "
                "such manner of reasoning in divine matters as immense toil has rendered deeply "
                "welcome to me.",
            ),
        ),
    ),
    BilingualSectionData(
        section_id="di-bk1-ch1",
        folio_prefix="DI I.1",
        heading_en="Book I, Chapter 1 — How To Know Is Not-To-Know",
        heading_la="Liber I, Capitulum I — Quomodo scire est ignorare",
        witness_note="h I, nn. 2–4 · Paris 1514 fol. 1r–1v · Rotta 1913 pp. 2–4",
        figure_svg=None,
        figure_caption=None,
        la_paragraphs=(
            (
                "DI I.1 §1",
                "Divino munere omnibus in rebus naturale quoddam desiderium inesse conspicimus, "
                "ut sint meliori quidem modo, quo hoc cuiusque naturae patitur condicio, atque ad "
                "hunc finem operari instrumentaque habere opportuna, quibus iudicium connatum est "
                "conveniens proposito cognoscendi, ne sit frustra appetitus et in amato pondere "
                "propriae naturae quietem attingere possit. Quod si fortassis secus contingat, hoc "
                "ex accidenti evenire necesse est, ut dum infirmitas gustum aut opinio rationem "
                "seducit. Quamobrem sanum liberum intellectum verum, quod insatiabiliter indito "
                "discursu cuncta perlustrando attingere cupit, apprehensum amoroso amplexu "
                "cognoscere dicimus non dubitantes verissimum illud esse, cui omnis sana mens "
                "nequit dissentire. Omnes autem investigantes in comparatione praesuppositi certi "
                "proportionabiliter incertum iudicant; comparativa igitur est omnis inquisitio "
                "medio proportionis utens. Et dum haec, quae inquiruntur, propinqua proportionali "
                "reductione praesupposito possunt comparari, facile est apprehensionis iudicium; "
                "dum multis mediis opus habemus, difficultas et labor exoritur; uti haec in "
                "mathematicis nota sunt, ubi ad prima notissima principia priores propositiones "
                "facilius reducuntur, et posteriores, quoniam non nisi per medium priorum, "
                "difficilius.",
            ),
            (
                "DI I.1 §2",
                "Omnis igitur inquisitio in comparativa proportione facili vel difficili existit; "
                "propter quod infinitum ut infinitum, cum omnem proportionem aufugiat, ignotum "
                "est. Proportio vero cum convenientiam in aliquo uno simul et alteritatem dicat, "
                "absque numero intelligi nequit. Numerus ergo omnia proportionabilia includit. Non "
                "est igitur numerus in quantitate tantum, qui proportionem efficit, sed in "
                "omnibus, quae quovismodo substantialiter aut accidentaliter convenire possunt ac "
                "differre. Hinc forte omnia Pythagoras per numerorum vim constitui et intelligi "
                "iudicabat. Praecisio vero combinationum in rebus corporalibus ac adaptatio "
                "congrua noti ad ignotum humanam rationem supergreditur, adeo ut Socrati visum sit "
                "se nihil scire, nisi quod ignoraret, sapientissimo Salomone asserente cunctas res "
                "difficiles et sermone inexplicabiles; et alius quidam divini spiritus vir ait "
                "absconditam esse sapientiam et locum intelligentiae ab oculis omnium viventium. "
                "Si igitur hoc ita est, ut etiam profundissimus Aristoteles in prima philosophia "
                "affirmat in natura manifestissimis talem nobis difficultatem accidere ut "
                "nocticoraci solem videre attemptanti, profecto, cum appetitus in nobis frustra "
                "non sit, desideramus scire nos ignorare. Hoc si ad plenum assequi poterimus, "
                "doctam ignorantiam assequemur. Nihil enim homini etiam studiosissimo in doctrina "
                "perfectius adveniet quam in ipsa ignorantia, quae sibi propria est, doctissimum "
                "reperiri; et tanto quis doctior erit, quanto se sciverit magis ignorantem. In "
                "quem finem de ipsa docta ignorantia pauca quaedam scribendi labores assumpsi.",
            ),
        ),
        en_paragraphs=(
            (
                "DI I.1 §1",
                "By a divine gift we observe implanted in all things a certain natural desire to "
                "exist in the best manner that the condition of each nature permits, and toward "
                "this end to act and to possess fitting instruments, within which an innate "
                "judgment is suited to the purpose of knowing, lest impulse be in vain and fail to "
                "reach rest in the beloved poise of its own nature. Should it perchance turn out "
                "otherwise, this must happen by accident, as when illness deceives taste or mere "
                "opinion misleads reason. Wherefore we say that a sound and free intellect knows "
                "the true—which it insatiably longs to reach by surveying all things through its "
                "inborn discursive motion—when it clasps what it has apprehended in a loving "
                "embrace, doubting not at all that to be most true from which no sound mind can "
                "dissent. Now all who investigate judge what is uncertain proportionally by "
                "comparing it with something presupposed as certain; every inquiry, therefore, is "
                "comparative and employs the medium of proportion. When the matters investigated "
                "can be compared to the presupposition by a close proportional reduction, the "
                "judgment of apprehension is easy; when we require many intermediate steps, "
                "difficulty and toil arise—just as is familiar in mathematics, where earlier "
                "propositions are led back quite easily to the first self-evident principles, "
                "whereas later propositions are reduced more arduously because only through the "
                "intermediation of the earlier ones.",
            ),
            (
                "DI I.1 §2",
                "Every inquiry, accordingly, consists in comparative proportion, whether easy or "
                "difficult; for which reason the infinite as infinite, since it escapes all "
                "proportion, remains unknown. Yet because proportion expresses agreement in some "
                "one respect together with otherness, it cannot be understood apart from number. "
                "Number therefore encompasses everything capable of proportion. Hence number "
                "produces proportion not in quantity alone, but in all things that can in any "
                "manner agree and differ, whether substantially or accidentally. Perhaps for this "
                "reason Pythagoras judged that all things are constituted and understood through "
                "the power of numbers. Nevertheless, exactness of combinations in bodily things "
                "and the precise adaptation of the known to the unknown surpass human reason—so "
                "much so that it seemed to Socrates that he knew nothing save that he was "
                "ignorant, while wisest Solomon declared all things difficult and beyond "
                "explanation in speech, and another man of divine spirit said that wisdom and the "
                "place of understanding are hidden from the eyes of all the living. If this is so—"
                "as even most profound Aristotle affirms in First Philosophy, that in the things "
                "most manifest by nature such difficulty befalls us as befalls a night-owl trying "
                "to gaze upon the sun—surely, since the desire within us is not in vain, what we "
                "desire is to know that we do not know. If we can attain this fully, we shall "
                "attain learned ignorance. For nothing more perfect will come even to the man most "
                "zealous in learning than to be found most learned in the very ignorance that is "
                "proper to him; and anyone will be the more learned the more he knows himself to "
                "be ignorant. Toward this end I have undertaken the labor of writing a few words "
                "concerning learned ignorance itself.",
            ),
        ),
    ),
    BilingualSectionData(
        section_id="di-bk1-ch2",
        folio_prefix="DI I.2",
        heading_en="Book I, Chapter 2 — Preliminary Elucidation of What Follows",
        heading_la="Liber I, Capitulum II — Elucidatio praeambularis subsequentium",
        witness_note="h I, nn. 5–8 · Paris 1514 fol. 1v–2r · Rotta 1913 pp. 5–6",
        figure_svg=None,
        figure_caption=None,
        la_paragraphs=(
            (
                "DI I.2 §1",
                "Tractaturus de maxima ignorantiae doctrina ipsius maximitatis naturam aggredi "
                "necesse habeo. Maximum autem hoc dico, quo nihil maius esse potest. Abundantia "
                "vero uni convenit. Coincidit itaque maximitati unitas, quae est et entitas. "
                "Quodsi ipsa talis unitas ab omni respectu et contractione universaliter est "
                "absoluta, nihil sibi opponi manifestum est, cum sit maximitas absoluta. Maximum "
                "itaque absolutum unum est, quod est omnia; in quo omnia, quia maximum. Et quoniam "
                "nihil sibi opponitur, secum simul coincidit minimum; quare et in omnibus; et quia "
                "absolutum, tunc est actu omne possibile esse, nihil a rebus contrahens, a quo "
                "omnia. Hoc maximum, quod et Deus omnium nationum fide indubie creditur, primo "
                "libello supra humanam rationem incomprehensibiliter inquirere eo duce, qui solus "
                "lucem inhabitat inaccessibilem, laborabo.",
            ),
            (
                "DI I.2 §2",
                "Secundo loco, sicut absoluta maximitas est entitas absoluta, per quam omnia id "
                "sunt, quod sunt, ita et universalis unitas essendi ab illa, quae maximum dicitur "
                "ab absoluto, et hinc contracte existens uti universum; cuius quidem unitas in "
                "pluralitate contracta est, sine qua esse nequit. Quod quidem maximum, etsi in sua "
                "universali unitate omnia complectatur, ut omnia, quae sunt ab absoluto, sint in "
                "eo et ipsum in omnibus, non habet tamen extra pluralitatem, in qua est, "
                "subsistentiam, cum sine contractione, a qua absolvi nequit, non existat. De hoc "
                "maximo, universo scilicet, in secundo libello pauca quaedam adiciam.",
            ),
            (
                "DI I.2 §3",
                "Tertio loco maximum tertiae considerationis subsequenter manifestabitur. Nam cum "
                "universum non habeat nisi contracte subsistentiam in pluralitate, in ipsis "
                "pluribus inquiremus unum maximum, in quo universum maxime et perfectissime "
                "subsistit actu ut in fine. Et quoniam tale cum absoluto, quod est terminus "
                "universalis, unitur, quia finis perfectissimus supra omnem capacitatem nostram, "
                "de illo maximo, quod simul est contractum et absolutum, quod Iesum semper "
                "benedictum nominamus, nonnulla, prout et ipse Iesus inspiraverit, subiciam.",
            ),
            (
                "DI I.2 §4",
                "Oportet autem attingere sensum volentem potius supra verborum vim intellectum "
                "efferre quam proprietatibus vocabulorum insistere, quae tantis intellectualibus "
                "mysteriis proprie adaptari non possunt. Exemplaribus etiam manuductionibus "
                "necesse est transcendenter uti, linquendo sensibilia, ut ad intellectualitatem "
                "simplicem expedite lector ascendat; ad quam viam quaerendam studui communibus "
                "ingeniis quanto clarius potui aperire, omnem stili scabrositatem evitando, "
                "radicem doctae ignorantiae in inapprehensibili veritatis praecisione statim "
                "manifestans.",
            ),
        ),
        en_paragraphs=(
            (
                "DI I.2 §1",
                "Being about to treat of the greatest doctrine of ignorance, I find it necessary "
                "to approach the very nature of maximality. Now I call 'Maximum' that than which "
                "nothing can be greater. Yet fullness belongs to the One. Unity, therefore—which "
                "is also beingness—coincides with maximality. And if such unity is universally "
                "absolved from every relation and contraction, it is manifest that nothing stands "
                "opposed to it, inasmuch as it is absolute maximality. Thus the Absolute Maximum "
                "is One, which is all things; in which all things are, because it is Maximum. "
                "Moreover, since nothing is opposed to it, the Minimum coincides with it at the "
                "same time; wherefore it is also in all things; and because it is absolute, it is "
                "in act all possible being, contracting nothing from things, while all things come "
                "from it. In the first little book I shall labor to investigate this Maximum—which "
                "by the indubitable faith of all nations is also believed to be God—"
                "incomprehensibly above human reason, guided by Him who alone dwells in light "
                "inaccessible.",
            ),
            (
                "DI I.2 §2",
                "In the second place, just as absolute maximality is absolute beingness through "
                "which all things are what they are, so too the universal unity of being derives "
                "from it—a unity called 'maximum from the Absolute' and hence existing "
                "contractedly as the universe, whose unity is contracted in plurality, apart from "
                "which it cannot exist. Although this maximum embraces all things within its "
                "universal unity, so that all things deriving from the Absolute are in it and it "
                "is in all of them, nevertheless it possesses no subsistence outside the plurality "
                "in which it exists, because it does not exist without contraction, from which it "
                "cannot be absolved. Concerning this maximum, namely the universe, I shall add a "
                "few remarks in the second book.",
            ),
            (
                "DI I.2 §3",
                "In the third place, the maximum of a third consideration will subsequently be "
                "made manifest. For since the universe has subsistence only contractedly in "
                "plurality, among those many things themselves we shall seek one maximum in which "
                "the universe subsists most greatly and most perfectly in act as in its goal. And "
                "because such a being is united with the Absolute, which is the universal bound, "
                "since it is the most perfect goal surpassing all our capacity, concerning that "
                "Maximum which is simultaneously contracted and absolute—whom we name Jesus, "
                "ever blessed—I shall subjoin certain reflections according as Jesus Himself "
                "shall inspire.",
            ),
            (
                "DI I.2 §4",
                "Whoever wishes to reach the meaning, however, must lift his intellect above the "
                "force of words rather than cling to the literal properties of terms, which cannot "
                "be fitted strictly to such great intellectual mysteries. Exemplary guidance too "
                "must be used transcendently, leaving sensible things behind so that the reader "
                "may swiftly ascend to simple intellectuality. To seek out this path I have "
                "striven to lay it open to ordinary minds as clearly as I could, shunning all "
                "harshness of style and revealing straightway that the root of learned ignorance "
                "lies in the ungraspable exactness of truth.",
            ),
        ),
    ),
    BilingualSectionData(
        section_id="di-bk1-ch3",
        folio_prefix="DI I.3",
        heading_en="Book I, Chapter 3 — That Precise Truth Is Incomprehensible",
        heading_la="Liber I, Capitulum III — Quod praecisa veritas sit incomprehensibilis",
        witness_note="h I, nn. 9–10 · Paris 1514 fol. 2r · Rotta 1913 pp. 7–8",
        figure_svg=None,
        figure_caption=None,
        la_paragraphs=(
            (
                "DI I.3 §1",
                "Quoniam ex se manifestum est infiniti ad finitum proportionem non esse, est et ex "
                "hoc clarissimum, quod, ubi est reperire excedens et excessum, non deveniri ad "
                "maximum simpliciter, cum excedentia et excessa finita sint. Maximum vero tale "
                "necessario est infinitum. Dato igitur quocumque, quod non sit ipsum maximum "
                "simpliciter, dabile maius esse manifestum est. Et quoniam aequalitatem reperimus "
                "gradualem, ut unum aequalius uni sit quam alteri secundum convenientiam et "
                "differentiam genericam, specificam, localem, influentialem et temporalem cum "
                "similibus: patet non posse aut duo aut plura adeo similia et aequalia reperiri, "
                "quin adhuc in infinitum similiora esse possint. Hinc mensura et mensuratum, "
                "quantumcumque aequalia, semper differentia remanebunt.",
            ),
            (
                "DI I.3 §2",
                "Non potest igitur finitus intellectus rerum veritatem per similitudinem praecise "
                "attingere. Veritas enim non est nec plus nec minus, in quodam indivisibili "
                "consistens, quam omne non ipsum verum existens praecise mensurare non potest; "
                "sicut nec circulum, cuius esse in quodam indivisibili consistit, non-circulus. "
                "Intellectus igitur, qui non est veritas, numquam veritatem adeo praecise "
                "comprehendit, quin per infinitum praecisius comprehendi possit, habens se ad "
                "veritatem sicut polygonia ad circulum, quae quanto inscripta plurium angulorum "
                "fuerit, tanto similior circulo, numquam tamen efficitur aequalis, etiamsi angulos "
                "in infinitum multiplicaverit, nisi in identitatem cum circulo se resolvat. Patet "
                "igitur de vero nos non aliud scire quam quod ipsum praecise, uti est, scimus "
                "incomprehensibile, veritate se habente ut absolutissima necessitate, quae nec "
                "plus aut minus esse potest quam est, et nostro intellectu ut possibilitate. "
                "Quidditas ergo rerum, quae est entium veritas, in sua puritate inattingibilis est "
                "et per omnes philosophos investigata, sed per neminem, uti est, reperta; et "
                "quanto in hac ignorantia profundius docti fuerimus, tanto magis ipsam accedimus "
                "veritatem.",
            ),
        ),
        en_paragraphs=(
            (
                "DI I.3 §1",
                "Because it is self-evident that there is no proportion of the infinite to the "
                "finite, from this it is likewise crystal clear that wherever one encounters "
                "exceeding and exceeded, one never arrives at the unqualified Maximum, since things "
                "that exceed and are exceeded are finite. Such a Maximum, by contrast, is "
                "necessarily infinite. Given anything whatsoever that is not the unqualified "
                "Maximum itself, it is manifest that a greater can be given. Moreover, because we "
                "find equality to exist by degrees—so that one thing is more equal to this than to "
                "that according to generic, specific, local, influential, and temporal agreement "
                "and difference, along with like conditions—it is plain that neither two nor more "
                "things can be found so similar and equal that they could not still be infinitely "
                "more similar. Hence measure and thing measured, however equal they may be, will "
                "forever remain distinct.",
            ),
            (
                "DI I.3 §2",
                "A finite intellect, therefore, cannot attain the truth of things with precision "
                "by means of likeness. For truth is neither more nor less, consisting in a certain "
                "indivisible, which nothing that is not the true itself can measure with exactness "
                "—just as what is not a circle cannot measure a circle, whose being consists in a "
                "certain indivisible. Thus the intellect, which is not truth, never comprehends "
                "truth so precisely that it could not be comprehended infinitely more precisely; "
                "for it stands to truth as an inscribed polygon stands to a circle: the more "
                "angles the inscribed polygon possesses, the more similar to the circle it becomes, "
                "yet it is never made equal to the circle, even if one multiplies its angles to "
                "infinity, unless it resolves itself into identity with the circle. Clearly, then, "
                "concerning the true we know nothing other than that we know it to be "
                "incomprehensible precisely as it is—truth standing as most absolute necessity, "
                "which can be neither more nor less than it is, and our intellect standing as "
                "possibility. Accordingly the quiddity of things, which is the truth of beings, is "
                "unattainable in its purity; though sought by every philosopher, by none has it "
                "been found as it is; and the more deeply we are schooled in this ignorance, the "
                "closer we draw to truth itself.",
            ),
        ),
    ),
    BilingualSectionData(
        section_id="di-bk1-ch4",
        folio_prefix="DI I.4",
        heading_en=(
            "Book I, Chapter 4 — The Absolute Maximum Is Incomprehensibly Understood, "
            "and with It the Minimum Coincides"
        ),
        heading_la=(
            "Liber I, Capitulum IV — Maximum absolutum incomprehensibiliter intelligitur; "
            "cum quo minimum coincidit"
        ),
        witness_note="h I, nn. 11–12 · Paris 1514 fol. 2r–2v · Rotta 1913 pp. 9–11",
        figure_svg=None,
        figure_caption=None,
        la_paragraphs=(
            (
                "DI I.4 §1",
                "Maximum, quo maius esse nequit, simpliciter et absolute cum maius sit, quam "
                "comprehendi per nos possit, quia est veritas infinita, non aliter quam "
                "incomprehensibiliter attingimus. Nam cum non sit de natura eorum, quae excedens "
                "admittunt et excessum, super omne id est, quod per nos concipi potest; omnia "
                "enim, quaecumque sensu, ratione aut intellectu apprehenduntur, intra se et ad "
                "invicem taliter differunt, quod nulla est aequalitas praecisa inter illa. Excedit "
                "igitur maxima aequalitas, quae a nullo est alia aut diversa, omnem intellectum; "
                "quare maximum absolute, cum sit omne id, quod esse potest, est penitus in actu; "
                "et sicut non potest esse maius, eadem ratione nec minus, cum sit omne id, quod "
                "esse potest. Minimum autem est, quo minus esse non potest. Et quoniam maximum est "
                "huiusmodi, manifestum est minimum maximo coincidere.",
            ),
            (
                "DI I.4 §2",
                "Et hoc tibi clarius fit, si ad quantitatem maximum et minimum contrahis. Maxima "
                "enim quantitas est maxime magna; minima quantitas est maxime parva. Absolve "
                "igitur a quantitate maximum et minimum – subtrahendo intellectualiter magnum et "
                "parvum –, et clare conspicis maximum et minimum coincidere; ita enim maximum est "
                "superlativus sicut minimum superlativus. Igitur absoluta maximitas non est magis "
                "maxima quam minima, quoniam in ipsa minimum est maximum coincidenter.",
            ),
            (
                "DI I.4 §3",
                "Oppositiones igitur his tantum, quae excedens admittunt et excessum, et his "
                "differenter conveniunt; maximo absolute nequaquam, quoniam supra omnem "
                "oppositionem est. Quia igitur maximum absolute est omnia absolute actu, quae esse "
                "possunt, taliter absque quacumque oppositione, ut in maximo minimum coincidat, "
                "tunc super omnem affirmationem est pariter et negationem. Et omne id, quod "
                "concipitur esse, non magis est quam non est; et omne id, quod concipitur non "
                "esse, non magis non est quam est. Sed ita est hoc, quod est omnia, et ita omnia, "
                "quod est nullum; et ita maxime hoc, quod est minime ipsum. Non enim aliud est "
                "dicere 'Deus, qui est ipsa maximitas absoluta, est lux,' quam ita 'Deus est "
                "maxime lux, quod est minime lux'. Aliter enim non esset maximitas absoluta omnia "
                "possibilia actu, si non foret infinita et terminus omnium et per nullum omnium "
                "terminabilis, prout in sequentibus ipsius Dei pietate explanabimus.",
            ),
            (
                "DI I.4 §4",
                "Hoc autem omnem nostrum intellectum transcendit, qui nequit contradictoria in suo "
                "principio combinare via rationis, quoniam per ea, quae nobis a natura manifesta "
                "fiunt, ambulamus; quae longe ab hac infinita virtute cadens ipsa contradictoria "
                "per infinitum distantia connectere simul nequit. Supra omnem igitur rationis "
                "discursum incomprehensibiliter absolutam maximitatem videmus infinitam esse, cui "
                "nihil opponitur, cum qua minimum coincidit. Maximum autem et minimum, ut in hoc "
                "libello sumuntur, transcendentes absolutae significationis termini existunt, ut "
                "supra omnem contractionem ad quantitatem molis aut virtutis in sua simplicitate "
                "absoluta omnia complectantur.",
            ),
        ),
        en_paragraphs=(
            (
                "DI I.4 §1",
                "Since the unqualified and Absolute Maximum, than which nothing can be greater, is "
                "greater than can be comprehended by us—because it is infinite truth—we attain it "
                "in no other way than incomprehensibly. For inasmuch as it does not belong to the "
                "nature of things that admit of exceeding and exceeded, it stands above everything "
                "that can be conceived by us; indeed, whatsoever things are apprehended by sense, "
                "reason, or intellect differ within themselves and from one another in such wise "
                "that there is no precise equality among them. Maximal equality, therefore, which "
                "is neither other than nor diverse from anything, surpasses every intellect. "
                "Wherefore the Absolute Maximum, since it is everything that can be, is wholly in "
                "act; and just as it cannot be greater, by the very same reason it cannot be "
                "lesser, since it is everything that can be. Now the Minimum is that than which "
                "nothing can be lesser. And because the Maximum is of just this kind, it is "
                "manifest that the Minimum coincides with the Maximum.",
            ),
            (
                "DI I.4 §2",
                "This becomes clearer to you if you contract maximum and minimum to quantity. For "
                "maximal quantity is maximally large, whereas minimal quantity is maximally small. "
                "Absolve, then, maximum and minimum from quantity—subtracting 'large' and 'small' "
                "intellectually—and you clearly behold that maximum and minimum coincide; for "
                "'maximum' is a superlative just as 'minimum' is a superlative. Absolute "
                "maximality, therefore, is no more maximal than minimal, because within it the "
                "minimum is the maximum coincidently.",
            ),
            (
                "DI I.4 §3",
                "Oppositions, accordingly, belong solely to things that admit of exceeding and "
                "exceeded, and to these in differing ways; to the Absolute Maximum they belong not "
                "at all, because it stands above all opposition. Since, then, the Absolute Maximum "
                "is absolutely in act all things that can be, without any opposition whatsoever so "
                "that in the Maximum the Minimum coincides, it likewise stands above every "
                "affirmation and negation. All that is conceived to be is no more than it is not; "
                "and all that is conceived not to be is not any more than it is. Rather, it is "
                "'this' in such a way that it is all things, and all things in such a way that it "
                "is none of them; and maximally 'this' in such a way that it is minimally the "
                "same. For to say 'God, who is absolute maximality itself, is light' is no other "
                "than to say 'God is maximally light in such wise that He is minimally light.' "
                "Otherwise absolute maximality would not be all possible things in act, were it "
                "not infinite and the bound of all things and boundable by none of them, as by "
                "God's own loving-kindness we shall explain in what follows.",
            ),
            (
                "DI I.4 §4",
                "Yet this transcends all our understanding, which cannot combine contradictories "
                "in their principle along the pathway of discursive reason, since we walk by way "
                "of things made manifest to us by nature; falling far short of this infinite "
                "power, reason cannot join together contradictories separated by an infinite "
                "distance. Above every discursive movement of reason, therefore, we see "
                "incomprehensibly that absolute maximality is infinite, that nothing is opposed to "
                "it, and that with it the Minimum coincides. 'Maximum' and 'Minimum,' as taken in "
                "this little book, stand as transcendent terms of absolute signification, so that "
                "above all contraction to quantity of bulk or of power they embrace all things in "
                "their absolute simplicity.",
            ),
        ),
    ),
    BilingualSectionData(
        section_id="di-epistola",
        folio_prefix="DI Ep.",
        heading_en="Author's Epistolary Colophon to Cardinal Julian (Kues, February 12, 1440)",
        heading_la="Epistola auctoris ad dominum Iulianum cardinalem (Cusa, XII. Februarii 1440)",
        witness_note="h I, nn. 263–264 · Paris 1514 fol. 25v · Rotta 1913 pp. 188–189",
        figure_svg=None,
        figure_caption=None,
        la_paragraphs=(
            (
                "DI Ep. §1",
                "Accipe nunc, pater metuende, quae iam dudum attingere variis doctrinarum viis "
                "concupivi, sed prius non potui, quousque in mari me ex Graecia redeunte, credo "
                "superno dono a patre luminum, a quo omne datum optimum, ad hoc ductus sum, ut "
                "incomprehensibilia incomprehensibiliter amplecterer in docta ignorantia, per "
                "transcensum veritatum corruptibilium humaniter scibilium. Quam nunc in eo, qui "
                "veritas est, absolvi his libellis, qui ex eodem principio artari possunt vel "
                "extendi. Debet autem in his profundis omnis nostri humani ingenii conatus esse, "
                "ut ad illam se elevet simplicitatem, ubi contradictoria coincidunt; in quo "
                "laborat prioris libelli conceptus. Secundus ex illo pauca de universo supra "
                "philosophorum communem viam elicit rara multis. Et nunc complevi finaliter "
                "tertium de Iesu superbenedicto libellum, ex eodem semper progrediens fundamento; "
                "et factus est mihi Iesus Dominus continue maior in intellectu et affectu per "
                "fidei crementum. Negare enim nemo potest Christi fidem habens, quod hac via in "
                "desiderio altius non inflammetur, ita ut post longas meditationes et ascensiones "
                "dulcissimum Iesum solum amandum videat et cum gaudio omnia linquens amplexetur ut "
                "vitam veram et gaudium sempiternum. Taliter intranti in Iesum omnia cedunt, et "
                "nihil ingerere possunt difficultatis quaecumque scripturae, neque hic mundus, "
                "quoniam in Iesum hic transformatur propter inhabitantem Christi spiritum in eo, "
                "qui est finis intellectualium desideriorum; quem tu, pater devotissime, supplici "
                "corde pro me miserrimo peccatore assidue exorare velis, ut pariter eo frui "
                "aeternaliter mereamur.",
            ),
            (
                "DI Ep. §2",
                "Complevi in Cusa 1440, XII. februarii.",
            ),
        ),
        en_paragraphs=(
            (
                "DI Ep. §1",
                "Receive now, revered father, the things that I long desired to attain by diverse "
                "pathways of learning yet could not reach before, until, while returning by sea "
                "from Greece, I was led—by a gift from on high, I believe, from the Father of "
                "lights, from whom comes every best gift—to embrace incomprehensible things "
                "incomprehensibly in learned ignorance, by transcending the corruptible truths "
                "knowable in a human manner. This learned ignorance I have now brought to "
                "completion, in Him who is Truth, within these little books, which from the self-"
                "same principle can be either condensed or expanded. In these deep matters the "
                "whole endeavor of our human mind ought to be to raise itself unto that simplicity "
                "where contradictories coincide: with this the conception of the first book "
                "labors. From that principle the second book draws forth a few insights concerning "
                "the universe, uncommon to many and above the ordinary road of philosophers. And "
                "now at last I have completed the third book concerning ever-blessed Jesus, "
                "advancing always from the same foundation; and the Lord Jesus has continually "
                "grown greater to me in intellect and affection through the increase of faith. For "
                "no one holding the faith of Christ can deny that along this path he is kindled "
                "higher in desire, so that after long meditations and ascents he sees most sweet "
                "Jesus alone as worthy of love and, joyfully forsaking all things, embraces Him as "
                "true life and everlasting joy. To one who thus enters into Jesus all things give "
                "way, and neither any writings whatsoever nor this world can cast up difficulty, "
                "because such a one is transformed into Jesus through the Spirit of Christ "
                "indwelling him, who is the goal of intellectual desires; whom do you, most "
                "devoted father, earnestly entreat with suppliant heart on behalf of me, a most "
                "wretched sinner, that together we may merit to enjoy Him eternally.",
            ),
            (
                "DI Ep. §2",
                "Completed at Kues, February 12, 1440.",
            ),
        ),
    ),
)


UNIT_2_SECTIONS: tuple[BilingualSectionData, ...] = (
    BilingualSectionData(
        section_id="di-bk1-ch11",
        folio_prefix="DI I.11",
        heading_en=(
            "Book I, Chapter 11 — That Mathematics Aids Us Most Greatly in "
            "Apprehending Diverse Divine Truths"
        ),
        heading_la=(
            "Liber I, Capitulum XI — Quod mathematica nos iuvet plurimum in "
            "diversorum divinorum apprehensione"
        ),
        witness_note="h I, nn. 30–32 · Paris 1514 fol. 4v–5r · Rotta 1913 pp. 23–25",
        figure_svg=None,
        figure_caption=None,
        la_paragraphs=(
            (
                "DI I.11 §1",
                "Consensere omnes sapientissimi nostri et divinissimi doctores visibilia veraciter "
                "invisibilium imagines esse atque creatorem ita cognoscibiliter a creaturis videri "
                "posse quasi in speculo et in aenigmate. Hoc autem, quod spiritualia – per se a "
                "nobis inattingibilia – symbolice investigentur, radicem habet ex his, quae "
                "superius dicta sunt, quoniam omnia ad se invicem quandam – nobis tamen occultam "
                "et incomprehensibilem – habent proportionem, ut ex omnibus unum exsurgat "
                "universum et omnia in uno maximo sint ipsum unum. Et quamvis omnis imago accedere "
                "videatur ad similitudinem exemplaris: tamen praeter maximam imaginem, quae est "
                "hoc ipsum, quod exemplar in unitate naturae, non est imago adeo similis aut "
                "aequalis exemplari, quin per infinitum similior et aequalior esse possit, uti iam "
                "ista ex superioribus nota facta sunt.",
            ),
            (
                "DI I.11 §2",
                "Quando autem ex imagine inquisitio fit, necesse est nihil dubii apud imaginem "
                "esse, in cuius transumptiva proportione incognitum investigatur, cum via ad "
                "incerta non nisi per praesupposita et certa esse possit. Sunt autem omnia "
                "sensibilia in quadam continua instabilitate propter possibilitatem materialem in "
                "ipsis abundantem. Abstractiora autem istis, ubi de rebus consideratio habetur, – "
                "non ut appendiciis materialibus, sine quibus imaginari nequeunt, penitus careant "
                "neque penitus possibilitati fluctuanti subsint – firmissima videmus atque nobis "
                "certissima, ut sunt ipsa mathematicalia. Quare in illis sapientes exempla "
                "indagandarum rerum per intellectum sollerter quaesiverunt, et nemo antiquorum, "
                "qui magnus habitus est, res difficiles alia similitudine quam mathematica "
                "aggressus est; ita ut Boethius, ille Romanorum litteratissimus, assereret neminem "
                "divinorum scientiam, qui penitus in mathematicis exercitio careret, attingere "
                "posse.",
            ),
            (
                "DI I.11 §3",
                "Nonne Pythagoras, primus et nomine et re philosophus, omnem veritatis "
                "inquisitionem in numeris posuit? Quem Platonici et nostri etiam primi in tantum "
                "secuti sunt, ut Augustinus noster et post ipsum Boethius affirmarent indubie "
                "numerum creandarum rerum in animo conditoris principale exemplar fuisse. Quomodo "
                "Aristoteles, qui singularis videri voluit priores confutando, aliter nobis in "
                "Metaphysicis specierum differentiam tradere potuit quam quod ipsas numeris "
                "compararet? Et idem dum de formis naturalibus, quomodo una sit in alia, scientiam "
                "tradere vellet, ad formas mathematicas necessario convolavit dicens: «Sicut "
                "trigonus in tetragono, ita inferior in superiori.» Taceo de innumeris exemplis "
                "suis similibus. Aurelius etiam Augustinus Platonicus, quando de quantitate animae "
                "et eiusdem immortalitate et ceteris altissimis investigavit, ad mathematica pro "
                "adiutorio convolavit. Ista via Boethio nostro adeo placere visa est, ut "
                "constanter assereret omnem veritatis doctrinam in multitudine et magnitudine "
                "comprehendi. Et si velis, ut compendiosius dicam: Nonne Epicurorum de atomis et "
                "inani sententia, quae et Deum negat et cunctam veritatem collidit, solum a "
                "Pytagoricis et Peripateticis mathematica demonstratione periit? Non posse "
                "scilicet ad atomos indivisibiles et simplices deveniri, quod ut principium "
                "Epicurus supposuit.",
            ),
            (
                "DI I.11 §4",
                "Hac veterum via incedentes, cum ipsis concurrentes dicimus, cum ad divina non "
                "nisi per symbola accedendi nobis via pateat, quod tunc mathematicalibus signis "
                "propter ipsorum incorruptibilem certitudinem convenientius uti poterimus.",
            ),
        ),
        en_paragraphs=(
            (
                "DI I.11 §1",
                "All our wisest and most divine teachers have agreed that visible things are truly "
                "images of invisible things and that the Creator can thus be seen recognizably "
                "from creatures as though in a mirror and in an enigma. Now the fact that "
                "spiritual realities—unattainable by us in themselves—may be investigated "
                "symbolically takes its root from what was said earlier: namely, that all things "
                "bear to one another a certain proportion (albeit hidden from us and "
                "incomprehensible), so that out of all things one universe arises and in the one "
                "Maximum all things are that very One. And although every image seems to approach "
                "likeness to its exemplar, nevertheless apart from the Maximal Image—which is the "
                "very thing the Exemplar is in unity of nature—no image is so similar or equal to "
                "its exemplar that it could not be infinitely more similar and equal, as has "
                "already become clear from the preceding chapters.",
            ),
            (
                "DI I.11 §2",
                "Whenever an inquiry proceeds from an image, however, nothing doubtful may remain "
                "within the image through whose transsumptive proportion the unknown is "
                "investigated, since the pathway to uncertain things can lead only through things "
                "presupposed and certain. Now all sensible things exist in a kind of continual "
                "instability owing to the material possibility abounding within them. Yet when "
                "objects more abstract than these are considered—not as wholly stripped of the "
                "material accompaniments without which they cannot be imagined, nor yet as wholly "
                "subject to fluctuating possibility—we see them to be most firm and most certain "
                "to us; such are mathematical entities themselves. Wherefore in them the wise "
                "skilfully sought examples of the realities to be searched out by the intellect, "
                "and none of the ancients esteemed as great approached difficult matters by any "
                "likeness other than the mathematical; so much so that Boethius, the most "
                "learned of the Romans, declared that no one wholly lacking practice in "
                "mathematics could attain knowledge of divine things.",
            ),
            (
                "DI I.11 §3",
                "Did not Pythagoras, the first philosopher both in name and in deed, place every "
                "investigation of truth in numbers? Him the Platonists and our own foremost "
                "thinkers followed so closely that our Augustine, and after him Boethius, affirmed "
                "beyond doubt that number was in the Creator's mind the principal exemplar of "
                "things to be created. How else could Aristotle—who wished to appear singular by "
                "refuting his predecessors—convey to us in the Metaphysics the difference of "
                "species save by comparing them to numbers? And when the same Aristotle wished to "
                "impart knowledge of natural forms, showing how one is contained in another, he "
                "necessarily fled to mathematical forms, saying: 'Just as the triangle is in the "
                "quadrangle, so the lower form is in the higher.' I pass over in silence countless "
                "similar examples of his. The Platonist Aurelius Augustine likewise, whenever he "
                "inquired into the magnitude of the soul, its immortality, and other loftiest "
                "themes, turned to mathematics for aid. This pathway so pleased our Boethius that "
                "he steadfastly asserted that every doctrine of truth is comprehended in multitude "
                "and magnitude. And if you wish me to speak still more concisely: did not the "
                "doctrine of the Epicureans concerning atoms and the void—which denies God and "
                "shatters all truth—perish at the hands of the Pythagoreans and Peripatetics "
                "solely by mathematical demonstration, namely that one cannot arrive at "
                "indivisible and simple atoms, which Epicurus had posited as his starting-point?",
            ),
            (
                "DI I.11 §4",
                "Walking along this road of the ancients and concurring with them, we say that, "
                "since no pathway for approaching divine realities lies open to us except through "
                "symbols, we shall be able to make all the more fitting use of mathematical signs "
                "on account of their incorruptible certitude.",
            ),
        ),
    ),
    BilingualSectionData(
        section_id="di-bk1-ch12",
        folio_prefix="DI I.12",
        heading_en=(
            "Book I, Chapter 12 — How Mathematical Signs Ought To Be Used for Our Purpose"
        ),
        heading_la=(
            "Liber I, Capitulum XII — Quomodo signis mathematicalibus sit utendum in proposito"
        ),
        witness_note="h I, nn. 33–34 · Paris 1514 fol. 5r · Rotta 1913 pp. 25–27",
        figure_svg=None,
        figure_caption=None,
        la_paragraphs=(
            (
                "DI I.12 §1",
                "Verum quoniam ex antehabitis constat maximum simpliciter nihil horum esse posse, "
                "quae per nos sciuntur aut concipiuntur, hinc, cum ipsum symbolice investigare "
                "proponimus, simplicem similitudinem transilire necesse est. Nam cum omnia "
                "mathematicalia sint finita et aliter etiam imaginari nequeant: si finitis uti pro "
                "exemplo voluerimus ad maximum simpliciter ascendendi, primo necesse est figuras "
                "mathematicas finitas considerare cum suis passionibus et rationibus, et ipsas "
                "rationes correspondenter ad infinitas tales figuras transferre, post haec tertio "
                "adhuc altius ipsas rationes infinitarum figurarum transumere ad infinitum simplex "
                "absolutissimum etiam ab omni figura. Et tunc nostra ignorantia "
                "incomprehensibiliter docebitur, quomodo de altissimo rectius et verius sit nobis "
                "in aenigmate laborantibus sentiendum.",
            ),
            (
                "DI I.12 §2",
                "Ita igitur agentes et sub directione maximae veritatis incipientes dicimus, quod "
                "sancti viri et elevatissimi ingenii, qui se figuris applicarunt, varie locuti "
                "sunt: Anselmus devotissimus veritatem maximam rectitudini infinitae comparavit; "
                "quem nos sequentes ad figuram rectitudinis, quam lineam rectam imaginor, "
                "convolemus. Alii peritissimi Trinitati superbenedictae triangulum trium aequalium "
                "et rectorum angulorum compararunt; et quoniam talis triangulus necessario est ex "
                "infinitis lateribus, ut ostendetur, dici poterit triangulus infinitus; et hos "
                "etiam sequemur. Alii, qui unitatem infinitam figurare nisi sunt, Deum circulum "
                "dixerunt infinitum. Illi vero, qui actualissimam Dei existentiam considerarunt, "
                "Deum quasi sphaeram infinitam affirmarunt. Nos autem istos omnes simul de maximo "
                "recte concepisse et unam omnium sententiam ostendemus.",
            ),
        ),
        en_paragraphs=(
            (
                "DI I.12 §1",
                "Yet since it is established from what has gone before that the unqualified "
                "Maximum can be none of the things known or conceived by us, when we propose to "
                "investigate it symbolically we must leap beyond simple likeness. For inasmuch as "
                "all mathematical objects are finite and cannot even be imagined otherwise, if we "
                "wish to use finite things as an example for ascending to the unqualified Maximum, "
                "first we must consider finite mathematical figures together with their properties "
                "and intelligible ratios; second, we must transfer those very ratios "
                "correspondingly to infinite figures of the same kind; and third, after this, we "
                "must transsume the ratios of those infinite figures still higher unto the Simple "
                "Infinite that is wholly absolved even from every figure. Then at last our "
                "ignorance will be taught incomprehensibly how we, who labor in an enigma, ought "
                "to think more rightly and more truly concerning the Most High.",
            ),
            (
                "DI I.12 §2",
                "Acting in this way, therefore, and setting out under the guidance of Maximal "
                "Truth, we note that holy men of most exalted mind who applied themselves to "
                "figures spoke in varied ways: most devout Anselm compared Maximal Truth to "
                "infinite rectitude; following him, let us turn to the figure of rectitude, which "
                "I picture as a straight line. Other very skilled thinkers compared to the "
                "superblessed Trinity a triangle of three equal and right angles; and because "
                "such a triangle necessarily consists of infinite sides, as will be shown, it may "
                "be called an infinite triangle—and these too we shall follow. Others, striving to "
                "figure infinite unity, called God an infinite circle. Those, finally, who "
                "contemplated the most actual existence of God affirmed God to be as it were an "
                "infinite sphere. We, however, shall demonstrate that all of these simultaneously "
                "conceived rightly concerning the Maximum, and that the judgment of them all is "
                "one and the same.",
            ),
        ),
    ),
)


UNIT_3_SECTIONS: tuple[BilingualSectionData, ...] = (
    BilingualSectionData(
        section_id="di-bk1-ch13",
        folio_prefix="DI I.13",
        heading_en="Book I, Chapter 13 — On the Properties of the Maximal and Infinite Line",
        heading_la="Liber I, Capitulum XIII — De passionibus lineae maximae et infinitae",
        witness_note=(
            "h I, nn. 35–36 · Paris 1514 fol. 5r–5v · Rotta 1913 pp. 27–29 "
            "(restoring Klibansky's collation on arc gh)"
        ),
        figure_svg=None,
        figure_caption=None,
        la_paragraphs=(
            (
                "DI I.13 §1",
                "Dico igitur, quod, si esset linea infinita, illa esset recta, illa esset "
                "triangulus, illa esset circulus et esset sphaera; et pariformiter, si esset "
                "sphaera infinita, illa esset circulus, triangulus et linea; et ita de triangulo "
                "infinito atque circulo infinito idem dicendum est.",
            ),
            (
                "DI I.13 §2",
                "Primum autem, quod linea infinita sit recta, patet: Diameter circuli est linea "
                "recta, et circumferentia est linea curva maior diametro; si igitur curva linea in "
                "sua curvitate recipit minus, quanto circumferentia fuerit maioris circuli, igitur "
                "circumferentia maximi circuli, quae maior esse non potest, est minime curva; "
                "quare maxime recta. Coincidit igitur cum maximo minimum, ita ut ad oculum "
                "videatur necessarium esse, quod maxima linea sit recta maxime et minime curva. "
                "Nec hic potest remanere scrupulus dubii, quando in figura hic lateraliter "
                "videtur, quomodo arcus cd maioris circuli plus recedit a curvitate quam arcus ef "
                "minoris circuli, et ille plus a curvitate recedit quam arcus gh adhuc minoris "
                "circuli; quare linea recta ab erit arcus maximi circuli, qui maior esse non "
                "potest. Et ita videtur, quomodo maxima et infinita linea necessario est "
                "rectissima, cui curvitas non opponitur, – immo curvitas in ipsa maxima linea est "
                "rectitudo; et hoc est primum probandum.",
            ),
            (
                "DI I.13 §3",
                "Secundo dictum est lineam infinitam triangulum maximum, circulum et sphaeram. Et "
                "ad hoc ostendendum oportet, ut in finitis lineis videamus, quid sit in potentia "
                "finitae lineae; et quia quidquid est in potentia finitae, hoc est infinita actu, "
                "erit nobis clarius id, quod inquirimus.",
            ),
            (
                "DI I.13 §4",
                "Et primo scimus, quod linea finita in longitudine potest esse longior et rectior, "
                "et iam probatum est maximam esse longissimam atque rectissimam. Secundo, si linea "
                "ab, remanente puncto a immobili, circumduceretur, quousque b veniret in c, ortus "
                "est triangulus; si perficitur circumductio, quousque b redeat ad initium, ubi "
                "incepit, fit circulus. Si iterum, a remanente immobili, b circumducitur, quousque "
                "perveniat ad locum oppositum, ubi incepit, qui sit d, est ex linea ab et ad "
                "effecta una continua linea et semicirculus descriptus. Et si, remanente bd "
                "diametro immobili, circumducatur semicirculus, exoritur sphaera; et ipsa sphaera "
                "est ultimum de potentia lineae, totaliter existens in actu, quoniam sphaera non "
                "est in potentia ad aliquam figuram ulteriorem. Si igitur in potentia lineae "
                "finitae sunt istae figurae, et linea infinita est omnia actu, ad quae finita est "
                "in potentia, sequitur infinitam esse triangulum, circulum et sphaeram. Quod erat "
                "probandum.",
            ),
            (
                "DI I.13 §5",
                "Et quia fortassis clarius hoc videre velles, quomodo ea, quae sunt in potentia "
                "finiti, est actu infinitum, adhuc de hoc te certissimum reddam.",
            ),
        ),
        en_paragraphs=(
            (
                "DI I.13 §1",
                "I declare, therefore, that if there were an infinite line, it would be a straight "
                "line, it would be a triangle, it would be a circle, and it would be a sphere; and "
                "in like manner, if there were an infinite sphere, it would be a circle, a "
                "triangle, and a line; and the very same must be said concerning an infinite "
                "triangle and an infinite circle.",
            ),
            (
                "DI I.13 §2",
                "First, that an infinite line is straight is plain: the diameter of a circle is a "
                "straight line, whereas the circumference is a curved line greater than the "
                "diameter. If, then, the curved line admits less curvature the larger the circle "
                "whose circumference it is, the circumference of the maximal circle—which cannot "
                "be greater—is minimally curved, and therefore maximally straight. Thus the "
                "Minimum coincides with the Maximum, so that before our very eyes it appears "
                "necessary that the maximal line be maximally straight and minimally curved. Nor "
                "can the slightest scruple of doubt linger here when in the figure alongside one "
                "sees how the arc cd of the larger circle recedes further from curvature than the "
                "arc ef of the smaller circle, and that arc recedes further from curvature than "
                "the arc gh of a still smaller circle; wherefore the straight line ab will be the "
                "arc of the maximal circle, which cannot be greater. Thus we see how a maximal and "
                "infinite line is necessarily most straight, to which curvature is not opposed—nay "
                "rather, within that maximal line itself curvature is rectitude; and this was the "
                "first point to be proved.",
            ),
            (
                "DI I.13 §3",
                "Second, it was stated that the infinite line is the maximal triangle, circle, and "
                "sphere. To demonstrate this, we must observe in finite lines what lies in the "
                "potency of a finite line; and because whatever lies in the potency of a finite "
                "line is what the infinite line is in act, what we seek will become clearer to us.",
            ),
            (
                "DI I.13 §4",
                "First we know that a finite line can be longer and straighter in length, and it "
                "has already been proved that the maximal line is longest and straightest. Second, "
                "if the line ab, while the point a remains fixed, is swung around until b arrives "
                "at c, a triangle arises; if the revolution is completed until b returns to the "
                "starting-point where it began, a circle is produced. Again, if while a remains "
                "fixed, b is swung around until it reaches the place opposite where it began—let "
                "it be d—from the lines ab and ad one continuous line is formed and a semicircle "
                "is described. And if, while the diameter bd remains fixed, the semicircle is "
                "revolved around it, a sphere arises; and this sphere itself is the ultimate "
                "realization of the potency of the line, existing wholly in act, because the "
                "sphere does not stand in potency toward any further figure. If, therefore, these "
                "figures reside in the potency of a finite line, and the infinite line is in act "
                "all things toward which a finite line is in potency, it follows that the infinite "
                "line is triangle, circle, and sphere. Which was to be proved.",
            ),
            (
                "DI I.13 §5",
                "And since perhaps you would wish to see still more clearly how the infinite is in "
                "act those things that lie in the potency of the finite, I shall render you most "
                "certain of this as well.",
            ),
        ),
    ),
    BilingualSectionData(
        section_id="di-bk1-ch14",
        folio_prefix="DI I.14",
        heading_en="Book I, Chapter 14 — That the Infinite Line Is a Triangle",
        heading_la="Liber I, Capitulum XIV — Quod infinita linea sit triangulus",
        witness_note=(
            "h I, nn. 37–39 · Paris 1514 fol. 5v–6r · Rotta 1913 pp. 30–31 "
            "(restoring Klibansky's collation on bd and dc)"
        ),
        figure_svg="cusa_flattening_triangles.svg",
        figure_caption=(
            "Book I, Chapter 14 — Flattening Isosceles Triangles T_n with Fixed Base BC = 2 and "
            "Apex A_n = (0, 1/n): Exact Rational Trigonometry Spreads s_A = 4n^2/(n^2+1)^2 -> 0 "
            "and Triple Quad Residual 16/n^2 -> 0 as T_n Resolves into Line BC."
        ),
        la_paragraphs=(
            (
                "DI I.14 §1",
                "Imaginativa, quae genus sensibilium non transcendit, non capit lineam posse "
                "triangulum esse, cum improportionabiliter ista in quantis differant. Erit tamen "
                "apud intellectum hoc facile. Nam iam constat non nisi unum possibile esse maximum "
                "et infinitum. Deinde constat – quoniam omnia duo latera cuiuslibet trianguli "
                "simul iuncta tertio minora esse non possunt – trianguli, cuius unum latus est "
                "infinitum, alia non esse minora. Et quia quaelibet pars infiniti est infinita, "
                "necessarium est omnem triangulum, cuius unum latus est infinitum, alia "
                "pariformiter esse infinita. Et quoniam plura infinita esse non possunt, "
                "transcendenter intelligis triangulum infinitum ex pluribus lineis componi non "
                "posse, licet sit maximus verissimus triangulus, incompositus et simplicissimus; "
                "et quia verissimus triangulus, qui sine tribus lineis esse nequit, erit "
                "necessarium ipsam unicam infinitam lineam esse tres et tres esse unam "
                "simplicissimam. Ita de angulis, quoniam non erit nisi angulus unus infinitus, et "
                "ille est tres anguli et tres anguli unus. Nec erit iste maximus triangulus ex "
                "lateribus et angulis compositus, sed unum et idem est linea infinita et angulus; "
                "ita quod et linea est angulus, quia triangulus linea.",
            ),
            (
                "DI I.14 §2",
                "Adhuc, poteris te iuvare ad huius intelligentiam per ascensionem a triangulo "
                "quanto ad non-quantum. Nam omnem triangulum quantum habere tres angulos aequales "
                "duobus rectis manifestum est; et ita, quanto unus angulus est maior, tanto alii "
                "minores. Et licet angulus unusquisque possit augeri usque ad duos rectos "
                "exclusive et non maxime secundum principium primum nostrum: admittamus tamen, "
                "quod maxime augeatur usque ad duos rectos inclusive, triangulo permanente. Tunc "
                "est manifestum triangulum unum angulum habere, qui est tres, et tres esse unum.",
            ),
            (
                "DI I.14 §3",
                "Pariformiter videre poteris triangulum lineam esse, quoniam, cum omnia duo latera "
                "trianguli quanti sint simul iuncta tanto tertio longiora, quanto angulus, quem "
                "faciunt, est duobus rectis minor, ut angulus bac quia duobus rectis multo est "
                "minor, hinc lineae ba et ac simul iunctae multo longiores bc. Igitur quanto "
                "angulus ille maior fuerit, ut bdc, tanto minus vincunt lineae bd et dc lineam bc, "
                "et superficies minor. Quare si per positionem angulus valeret duos rectos, "
                "resolveretur in lineam simplicem totus triangulus. Unde cum hac positione, quae "
                "in quantis impossibilis est, iuvare te potes ad non-quanta ascendendo; in quibus, "
                "quod in quantis est impossibile, vides per omnia necessarium. Et in hoc patet "
                "lineam esse infinitam triangulum maximum. Quod erat ostendendum.",
            ),
        ),
        en_paragraphs=(
            (
                "DI I.14 §1",
                "The imaginative power, which does not transcend the genus of sensible things, "
                "does not grasp how a line can be a triangle, since among magnitudes these differ "
                "without proportion. For the intellect, however, this will prove easy. For it has "
                "already been established that only one Maximum and Infinite is possible. Next it "
                "is established—because any two sides of whatever triangle taken together cannot "
                "be lesser than the third—that in a triangle of which one side is infinite, the "
                "remaining sides are not lesser. And since every part of the infinite is infinite, "
                "for every triangle having one infinite side the other sides must likewise be "
                "infinite. Moreover, since there cannot be several infinites, you understand "
                "transcendently that an infinite triangle cannot be compounded out of several "
                "lines, even though it is the maximal and truest triangle, uncompounded and most "
                "simple; and because it is the truest triangle, which cannot exist without three "
                "lines, that single infinite line itself will necessarily be three, and the three "
                "will be one most simple line. And so too regarding angles: for there will be only "
                "one infinite angle, and that angle is three angles, and the three angles are one. "
                "Nor will this maximal triangle be compounded of sides and angles, but infinite "
                "line and angle are one and the same, so that line is also angle because triangle "
                "is line.",
            ),
            (
                "DI I.14 §2",
                "Furthermore, you can aid yourself toward understanding this by ascending from a "
                "quantified triangle to a non-quantified one. Clearly every quantified triangle "
                "has three angles equal to two right angles; hence the larger one angle is, the "
                "smaller are the others. And although any one angle can be enlarged up to two "
                "right angles exclusively—and never maximally, according to our first principle—"
                "let us nevertheless admit by supposition that it is enlarged maximally right up "
                "to two right angles inclusively while the triangle remains. Then it is manifest "
                "that the triangle has one angle that is three, and that the three are one.",
            ),
            (
                "DI I.14 §3",
                "In like manner you can see that a triangle is a line: because any two sides of a "
                "quantified triangle taken together exceed the third side all the more according "
                "as the angle they form is much less than two right angles—for instance, because "
                "the angle bac is much smaller than two right angles, the lines ba and ac joined "
                "together are much longer than bc—therefore, the larger that apex angle becomes, "
                "such as bdc, the less do the lines bd and dc surpass the line bc, and the smaller "
                "is the enclosed area. Wherefore, if by supposition the angle were equal to two "
                "right angles, the entire triangle would resolve into a simple line. Hence by "
                "means of this supposition, which among quantified things is impossible, you can "
                "aid yourself in ascending to non-quantified realities, among which what is "
                "impossible in quantities you behold to be altogether necessary. And herein it is "
                "plain that the infinite line is the maximal triangle. Which was to be shown.",
            ),
        ),
    ),
    BilingualSectionData(
        section_id="di-bk1-ch15",
        folio_prefix="DI I.15",
        heading_en="Book I, Chapter 15 — That That Triangle Is a Circle and a Sphere",
        heading_la="Liber I, Capitulum XV — Quod ille triangulus sit circulus et sphaera",
        witness_note="h I, nn. 40–41 · Paris 1514 fol. 6r · Rotta 1913 pp. 31–32",
        figure_svg="cusa_mobius_inversion.svg",
        figure_caption=(
            "Book I, Chapters 13 & 15 — Projective-Conformal Realization via Unit-Circle "
            "Inversion at Pole S = (0, -1): Every Tangent Circle C_R Maps to a Finite Rational "
            "Circle C'_R Converging Smoothly to C'_inf at (0, -1/2), Radius 1/2—Identical to "
            "the Inverted Tangent Line AB."
        ),
        la_paragraphs=(
            (
                "DI I.15 §1",
                "Deinde clarius videbitur triangulum esse circulum. Nam sit triangulus abc "
                "causatus per positionem, per circumductionem lineae ab, quousque b venit in c, a "
                "fixo remanente: Non habet dubium, quando linea ab esset infinita et penitus "
                "circumduceretur b, quousque rediret ad initium, circulum maximum causari, cuius "
                "bc est portio. Et quia est portio arcus infiniti, tunc est linea recta bc. Et "
                "quoniam omnis pars infiniti est infinita, igitur bc non est minor integro arcu "
                "circumferentiae infinitae. Erit igitur bc non tantum portio, sed completissima "
                "circumferentia. Quare necessarium est triangulum abc esse circulum maximum.",
            ),
            (
                "DI I.15 §2",
                "Et quia bc circumferentia est linea recta, non est maior ab infinitae, cum "
                "infinito non sit maius. Nec sunt duae lineae, quia duo infinita esse non possunt. "
                "Quare linea infinita, quae est triangulus, est etiam circulus. Quod fuit "
                "propositum.",
            ),
            (
                "DI I.15 §3",
                "Adhuc, quod linea infinita sit sphaera, ita manifestissimum fit: Linea ab est "
                "circumferentia maximi circuli, – immo et circulus, ut iam probatum est; et est in "
                "triangulo de b ducta in c, ut supra dictum est. Sed bc est infinita linea, ut "
                "etiam statim probatum est. Quare ab rediit in c, supra se reditione completa. Et "
                "quando hoc est, sequitur sphaeram necessario exortam ex tali revolutione circuli "
                "supra se. Et quia supra probatum est abc esse circulum, triangulum et lineam, "
                "habemus nunc probatum esse etiam sphaeram. Et ista sunt, quae investigare "
                "proposuimus.",
            ),
        ),
        en_paragraphs=(
            (
                "DI I.15 §1",
                "Next it will be seen still more clearly that this triangle is a circle. Let the "
                "triangle abc be generated by supposition through swinging the line ab around "
                "while a remains fixed until b arrives at c. Beyond doubt, if the line ab were "
                "infinite and b were swung completely around until it returned to its starting-"
                "point, a maximal circle would be generated, of which bc is a portion. Now because "
                "bc is a portion of an infinite arc, bc is a straight line. And since every part "
                "of the infinite is infinite, bc is therefore not smaller than the whole arc of "
                "the infinite circumference. Hence bc will be not merely a portion, but the most "
                "complete circumference itself. Consequently the triangle abc must be the maximal "
                "circle.",
            ),
            (
                "DI I.15 §2",
                "Moreover, because the circumference bc is a straight line, it is not greater than "
                "the infinite line ab, since nothing is greater than the infinite; nor are there "
                "two lines, because there cannot be two infinites. Therefore the infinite line, "
                "which is a triangle, is also a circle. Which was proposed.",
            ),
            (
                "DI I.15 §3",
                "Furthermore, that the infinite line is a sphere becomes utterly manifest as "
                "follows: the line ab is the circumference of the maximal circle—nay rather, it is "
                "the circle itself, as has already been proved—and in the triangle it was carried "
                "from b to c, as stated above. Yet bc is the infinite line, as has likewise just "
                "been proved. Therefore ab has returned upon itself in c with a complete return "
                "upon itself. And when this happens, it follows of necessity that a sphere has "
                "arisen from such a revolution of a circle upon itself. Because it was proved "
                "above that abc is circle, triangle, and line, we have now proved that it is also "
                "a sphere. And these are the things we set out to investigate.",
            ),
        ),
    ),
)
