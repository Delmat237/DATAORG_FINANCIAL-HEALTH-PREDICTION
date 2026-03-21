En machine learning, la différence entre l'accuracy (exactitude ou justesse) et la précision réside dans ce que l'on cherche à mesurer : la performance globale ou la fiabilité d'une prédiction spécifique. [1, 2] 
1. L'Accuracy (Justesse)
L'accuracy mesure la performance globale du modèle. Elle répond à la question : « Sur l'ensemble des prédictions, combien sont correctes ? ». [3, 4, 5] 

* Calcul : $\text{Accuracy} = \frac{\text{Vrais Positifs} + \text{Vrais Négatifs}}{\text{Nombre total de prédictions}}$.
* Utilisation : Elle est idéale lorsque les classes sont équilibrées (autant d'exemples de chaque catégorie).
* Piège : Elle peut être trompeuse sur des jeux de données déséquilibrés. Si 95 % de vos e-mails ne sont pas des spams, un modèle qui prédit toujours "non-spam" aura 95 % d'accuracy sans rien détecter du tout. [4, 5, 6] 

2. La Précision
La précision mesure la fiabilité du modèle lorsqu'il annonce un résultat positif. Elle répond à la question : « Quand le modèle dit que c'est positif, à quel point est-ce vrai ? ». [4, 5, 7, 8] 

* Calcul : $\text{Précision} = \frac{\text{Vrais Positifs}}{\text{Vrais Positifs} + \text{Faux Positifs}}$.
* Utilisation : Elle est cruciale lorsque le coût d'un "Faux Positif" est élevé. Par exemple, dans un filtre antispam, on veut une haute précision pour éviter qu'un e-mail important ne soit classé par erreur dans les spams. [4, 7, 9, 10, 11] 

Comparaison par l'analogie de la cible
On utilise souvent l'image d'une cible pour illustrer ces concepts : [12] 

* Haute Accuracy : Les flèches arrivent globalement autour du centre.
* Haute Précision : Les flèches arrivent toutes au même endroit, même s'il est éloigné du centre (reproductibilité). [13, 14, 15] 

Souhaitez-vous également comprendre le concept de recall (rappel), qui complète souvent la précision ?

[1] [https://www.evidentlyai.com](https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall)
[2] [https://www.ultralytics.com](https://www.ultralytics.com/blog/accuracy-precision-recall)
[3] [https://encord.com](https://encord.com/blog/classification-metrics-accuracy-precision-recall/)
[4] [https://www.linkedin.com](https://www.linkedin.com/posts/%F0%9D%98%BE%F0%9D%99%83%F0%9D%99%80%F0%9D%99%8F%F0%9D%98%BC%F0%9D%99%89-%F0%9D%99%86%F0%9D%99%8A%F0%9D%99%86%F0%9D%98%BC%F0%9D%99%8F%F0%9D%99%89%F0%9D%99%90%F0%9D%99%8D%F0%9D%99%80-38aa62115_accuracy-vs-precision-explained-with-activity-7427183425683431424-fVsx)
[5] [https://www.youtube.com](https://www.youtube.com/shorts/lyeKdKwfp9w)
[6] [https://nugg.ad](https://nugg.ad/fr/glossaire-ia/precision-machine-learning/#:~:text=La%20formule%20math%C3%A9matique%20de%20la%20pr%C3%A9cision%20La,correctes%20et%20incorrectes%20dans%20toutes%20les%20cat%C3%A9gories.)
[7] [https://developers.google.com](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall)
[8] [https://www.monshotdata.com](https://www.monshotdata.com/p/cheat-sheet-ultime-des-metriques-de-performance-en-machine-learning#:~:text=Precision%20%28pr%C3%A9cision%29%20:%20*%20Mesure%20la%20proportion,du%20mod%C3%A8le%20lorsqu%27il%20pr%C3%A9dit%20une%20classe%20positive.)
[9] [https://medium.com](https://medium.com/data-science/accuracy-precision-recall-or-f1-331fb37c5cb9)
[10] [https://developers.google.com](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall?hl=fr#:~:text=Choix%20de%20la%20m%C3%A9trique%20et%20compromis%20M%C3%A9trique,pr%C3%A9cision%20des%20pr%C3%A9dictions%20positives%20est%20tr%C3%A8s%20importante.)
[11] [https://www.linkedin.com](https://www.linkedin.com/advice/0/heres-how-you-can-calculate-precision-recall-machine-8dh9c?lang=fr#:~:text=Cette%20mesure%20est%20particuli%C3%A8rement%20importante%20dans%20les,qui%20peut%20entra%C3%AEner%20la%20n%C3%A9gligence%20d%27informations%20importantes.)
[12] [https://deepchecks.com](https://deepchecks.com/question/what-is-the-difference-between-precision-and-accuracy/)
[13] [https://www.quora.com](https://www.quora.com/What-is-the-difference-between-precision-and-accuracy-in-machine-learning)
[14] [https://ims.evidentscientific.com](https://ims.evidentscientific.com/fr/insights/accuracy-vs-precision-in-handheld-xrf-whats-the-difference#:~:text=La%20pr%C3%A9cision%2C%20c%27est%20la%20mesure%20de%20r%C3%A9p%C3%A9tabilit%C3%A9%2C,r%C3%A9sultat%20%C2%AB%20frappe%20dans%20le%20mille%20%C2%BB.)
[15] [https://www.precisa.com](https://translate.google.com/translate?u=https://www.precisa.com/article/what-is-the-difference-between-accuracy-and-precision-measurements/&hl=fr&sl=en&tl=fr&client=sge#:~:text=L%27exactitude%20indique%20%C3%A0%20quel%20point%20une%20mesure,r%C3%A9p%C3%A9tables%20et%20tr%C3%A8s%20proches%20des%20valeurs%20r%C3%A9elles.)



Le rappel (ou recall en anglais) mesure la capacité de votre modèle à détecter tous les cas positifs réels. [1, 2] 
Alors que la précision se concentre sur la "qualité" (ne pas se tromper quand on prédit un positif), le rappel se concentre sur la "quantité" (ne pas oublier de cas positifs). [3] 
1. Définition et calcul
Le rappel répond à la question : « Sur tous les individus qui sont réellement positifs, combien mon modèle a-t-il réussi à en trouver ? ». [4, 5] 

* Calcul : $\text{Rappel} = \frac{\text{Vrais Positifs}}{\text{Vrais Positifs} + \text{Faux Négatifs}}$.
* Un rappel élevé signifie que vous avez très peu de faux négatifs (des cas que vous avez ratés). [6, 7, 8, 9] 

2. Pourquoi est-ce important ?
Le rappel est la métrique prioritaire lorsque rater un cas positif est grave, même si cela signifie faire quelques fausses alertes (baisser la précision). [1] 

* Exemple médical : Dans un test de dépistage d'une maladie grave, on veut un rappel de 100 %. Il vaut mieux tester plus de personnes par erreur (faux positifs) que de laisser partir un patient malade sans traitement (faux négatif).
* Détection de fraudes : Une banque préfère bloquer temporairement une carte par erreur (basse précision) plutôt que de laisser passer un vol réel (bas rappel). [10, 11] 

3. Le dilemme Précision vs Rappel
Il existe souvent un compromis : si vous élargissez vos critères pour "rattraper" tout le monde (augmenter le rappel), vous risquez d'inclure plus d'erreurs (baisser la précision). [12] 

| Métrique [10, 11] | Question clé | Risque principal |
|---|---|---|
| Précision | Est-ce que ce que j'ai trouvé est correct ? | Les faux positifs (fausses alertes) |
| Rappel | Est-ce que j'ai trouvé tout le monde ? | Les faux négatifs (oublis) |

Pour équilibrer ces deux notions, on utilise souvent le [F1-Score sur Evidently AI](https://www.evidentlyai.com.en2fr.search.translate.goog/classification-metrics/accuracy-precision-recall), qui est la moyenne harmonique des deux. [9, 13] 
Souhaitez-vous voir un exemple concret avec une matrice de confusion pour visualiser ces erreurs ?

[1] [https://www.nexa.fr](https://www.nexa.fr/blog/recall-definition)
[2] [https://www.nexa.fr](https://www.nexa.fr/blog/recall-definition#:~:text=Le%20recall%20est%20une%20mesure%20de%20performance,les%20occurrences%20positives%20d%27un%20jeu%20de%20donn%C3%A9es.)
[3] [https://en.wikipedia.org](https://translate.google.com/translate?u=https://en.wikipedia.org/wiki/Precision_and_recall&hl=fr&sl=en&tl=fr&client=sge#:~:text=La%20pr%C3%A9cision%20peut%20%C3%AAtre%20consid%C3%A9r%C3%A9e%20comme%20une,comme%20une%20mesure%20de%20la%20quantit%C3%A9%20.)
[4] [https://www.evidentlyai.com](https://translate.google.com/translate?u=https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall&hl=fr&sl=en&tl=fr&client=sge#:~:text=Le%20rappel%20est%20une%20mesure%20qui%20%C3%A9value,positifs%20par%20le%20nombre%20d%27instances%20positives%20.)
[5] [https://www.youtube.com](https://www.youtube.com/shorts/67Ekk-rM5dE)
[6] [https://fr.scribd.com](https://fr.scribd.com/document/722532233/AHMED-YASSINE-METKOUL)
[7] [https://www.britannica.com](https://translate.google.com/translate?u=https://www.britannica.com/science/precision-and-recall&hl=fr&sl=en&tl=fr&client=sge#:~:text=Le%20rappel%20est%20calcul%C3%A9%20en%20divisant%20le,=%20VP%20/%20%28VP%20+%20FN%29%20.)
[8] [https://www.flowhunt.io](https://www.flowhunt.io/fr/glossaire/recall-in-machine-learning/#:~:text=Un%20rappel%20%C3%A9lev%C3%A9%20implique%20un%20faible%20taux,type%20II%2C%20donc%20peu%20de%20faux%20n%C3%A9gatifs.)
[9] [https://towardsdatascience.com](https://translate.google.com/translate?u=https://towardsdatascience.com/finally-remember-what-precision-and-recall-is-and-stop-being-afraid-of-these-questions-in-f61981930c67/&hl=fr&sl=en&tl=fr&client=sge#:~:text=Une%20pr%C3%A9cision%20%C3%A9lev%C3%A9e%20signifie%20un%20faible%20taux,et%20le%20rappel%20en%20un%20seul%20chiffre.)
[10] [https://www.analyticsvidhya.com](https://translate.google.com/translate?u=https://www.analyticsvidhya.com/blog/2024/06/data-science-in-medicine/&hl=fr&sl=en&tl=fr&client=sge#:~:text=La%20pr%C3%A9cision%20mesure%20l%27exactitude%20des%20pr%C3%A9dictions%20positives%2C,les%20vrais%20n%C3%A9gatifs%20dans%20les%20tests%20m%C3%A9dicaux.)
[11] [https://learn.snyk.io](https://translate.google.com/translate?u=https://learn.snyk.io/lesson/false-negatives-and-false-positives/&hl=fr&sl=en&tl=fr&client=sge#:~:text=Les%20faux%20n%C3%A9gatifs%20se%20produisent%20lorsqu%27il%20existe,s%27agit%20en%20r%C3%A9alit%C3%A9%20d%27un%20trafic%20utilisateur%20normal.)
[12] [https://fr.linkedin.com](https://fr.linkedin.com/pulse/importance-recall-machine-learning-why-matters-how-improve-kumar-be3sc?tl=fr)
[13] [https://keylabs.ai](https://translate.google.com/translate?u=https://keylabs.ai/blog/using-a-confusion-matrix-to-calculate-precision-and-recall/&hl=fr&sl=en&tl=fr&client=sge#:~:text=Pr%C3%A9cision%20:%20TP%20/%20%28TP%20+%20FP%29,/%20%28Pr%C3%A9cision%20+%20Rappel%29%20=%2075%20%25)
