<!-- R1 -->
<h2>Mise à Jour de la Documentation des Accès et des Règles de Partage en Conformité avec le RGPD</h2>

<h3>Introduction</h3>
<p>Le présent document vise à décrire les mesures prises pour mettre à jour le registre des traitements de données personnelles dans le cadre de la collecte et de l'analyse de données d'utilisateurs du site Mastodon. Ces mesures sont prises dans le but de se conformer au Règlement Général sur la Protection des Données (RGPD) de l'Union européenne, qui impose des règles strictes concernant le traitement des données personnelles.</p>

<h3>Description des Champs</h3>
<ul>
  <li><b>id : </b>Identifiant unique du message.</li>
  <li><b>created_at: </b>Date de création du message au format UNIX timestamp.</li>
  <li><b>in_reply_to_id: </b>Identifiant du message auquel ce message répond, le cas échéant.</li>
  <li><b>in_reply_to_account_id: </b>Identifiant du compte auquel ce message répond, le cas échéant.</li>
  <li><b>sensitive: </b>Indique si le contenu du message est sensible (true/false).</li>
  <li><b>spoiler_text: </b>Texte de mise en garde, le cas échéant.</li>
  <li><b>visibility: </b>Niveau de visibilité du message (public, unlisted, etc.).</li>
  <li><b>language: </b>Langue du message.</li>
  <li><b>uri: </b>URI du message sur Mastodon.</li>
  <li><b>replies_count: </b>Nombre de réponses au message.</li>
  <li><b>reblogs_count: </b>Nombre de reblogs (partages) du message.</li>
  <li><b>favourites_count: </b>Nombre de favoris (likes) du message.</li>
  <li><b>edited_at: </b>Date de dernière édition du message.</li>
  <li><b>content: </b>Contenu du message au format HTML.</li>
  <li><b>reblog: </b>Informations sur le reblog, le cas échéant.</li>
  <li><b>application: </b>Informations sur l'application qui a créé le message.</li>
  <li><b>account: </b>Informations sur le compte utilisateur qui a créé le message.</li>
  <li><b>media_attachments: </b>Informations sur les pièces jointes multimédias, le cas échéant.</li>
  <li><b>mentions: </b>Mentions d'autres utilisateurs dans le message.</li>
  <li><b>tags: </b>Tags associés au message.</li>
  <li><b>emojis: </b>Emojis utilisés dans le message.</li>
  <li><b>card: </b>Informations de carte, le cas échéant.</li>
  <li><b>poll: </b>Sondage associé au message, le cas échéant.</li>
</ul>

<h3>Mise à Jour de la Documentation</h3>

<p>La documentation des accès et des règles de partage a été révisée et mise à jour pour refléter les meilleures pratiques en matière de protection des données personnelles et de respect de la vie privée des utilisateurs. Voici les principales étapes de cette mise à jour :</p>

<ol>
  <li><h4>Identification des Données Personnelles Partagées</h4> <p>La documentation a été mise à jour pour identifier de manière exhaustive les types de données personnelles partagées dans le cadre de la collecte de données sur le site Mastodon. Cela inclut une description détaillée des catégories de données, des finalités du partage, des destinataires, etc.</p></li>
  <li><h4>Bases Légales du Partage</h4> <p>Chaque élément de la documentation spécifie clairement les bases légales sur lesquelles le partage de données personnelles repose, conformément aux exigences du RGPD.</p></li>
  <li><h4>Permissions et Consentement</h4> <p>Les procédures pour obtenir le consentement des utilisateurs, le cas échéant, sont documentées. Les méthodes pour gérer les préférences de consentement sont également décrites.</p></li>
  <li><h4>Sécurité des Données</h4> <p>La documentation inclut des informations détaillées sur les mesures de sécurité mises en place pour protéger les données personnelles partagées.</p></li>
  <li><h4>Durées de Conservation</h4> <p>Les durées de conservation des données partagées sont spécifiées, en accord avec les dispositions du RGPD.</p></li>
  <li><h4>Règles de Partage avec les Tiers</h4> <p>Les règles de partage de données avec des tiers, le cas échéant, sont clairement énoncées. Cela inclut les contrats de traitement de données et les engagements de conformité au RGPD.</p></li>
</ol>

<!-- R2 -->

<h2>Programmation des Évolutions et des Nouvelles Procédures d'Alimentation Automatisées</h2>
<h3>Programmation des Évolutions</h3>
<p>Le processus de programmation des évolutions comprend les étapes suivantes :</p>

<ol>
  <li><h4>Identification des Évolutions Nécessaires</h4><p>Nous avons identifié les évolutions nécessaires pour améliorer notre système de collecte et d'analyse de données. Cela inclut l'ajout de nouvelles fonctionnalités, la correction de bogues, et l'optimisation des performances.</p></li>
  <li><h4>Planification des Évolutions</h4><p>Chaque évolution a été planifiée en détail, y compris les ressources nécessaires, les délais, et les responsabilités. Nous nous assurons que chaque évolution est alignée avec nos objectifs et notre calendrier.</p></li>
  <li><h4>Développement et Tests</h4><p>Les évolutions sont développées, puis soumises à des tests rigoureux pour garantir leur bon fonctionnement et leur compatibilité avec les autres composants du système.</p></li>
  <li><h4>Intégration dans les DAGs</h4><p>Les évolutions sont intégrées dans nos Directed Acyclic Graphs (DAGs) Airflow, qui orchestrent le traitement de données. Cela inclut la mise à jour de tâches existantes et l'ajout de nouvelles tâches pour gérer les nouvelles fonctionnalités.</p></li>
</ol>

<h3>Nouvelles Procédures d'Alimentation Automatisées</h3>
<p>L'automatisation de l'alimentation des données est essentielle pour maintenir nos données à jour et garantir leur précision. Voici comment nous gérons ces procédures :</p>

<ol>
  <li><h4>Définition des Fréquences d'Alimentation</h4><p>Nous avons défini des fréquences appropriées pour chaque DAG Airflow, en tenant compte de la fréquence de rafraîchissement des données sur le site Mastodon.</p></li>
  <li><h4>Gestion des Flux de Données</h4><p>Les flux de données sont gérés pour assurer un transfert fiable des données depuis Mastodon vers notre environnement de traitement.</p></li>
  <li><h4>Surveillance et Alertes</h4><p>Nous avons mis en place des systèmes de surveillance et d'alertes pour détecter toute anomalie ou échec dans les procédures d'alimentation automatisées.</p></li>
</ol>

<!-- R3 -->

<h2>Mise à jour du Registre des Traitements de Données Personnelles en Conformité avec le RGPD</h2>

    
<h3>Mise à Jour du Registre des Traitements</h3>
<p>Le registre des traitements de données personnelles a été initialement établi pour recenser l'ensemble des traitements de données personnelles effectués au sein de notre organisation. Il est essentiel de maintenir ce registre à jour pour refléter tout nouveau traitement de données personnelles, y compris la collecte et l'analyse des données d'utilisateurs de Mastodon.</p>

<ol>
  <li><h4>Identification des Traitements de Données</h4>
  <p>Le registre a été mis à jour pour inclure une section spécifique identifiant les traitements de données liés à la collecte de données sur le site Mastodon. Chaque traitement est documenté en détail, y compris les objectifs, les catégories de données personnelles traitées, les bases légales du traitement, les périodes de conservation, etc.</p></li>
  
  <li>
  <h4>Analyse d'Impact sur la Protection des Données (AIPD)</h4>
  <p>Pour les traitements de données les plus sensibles ou à haut risque, une Analyse d'Impact sur la Protection des Données (AIPD) a été réalisée. Les résultats de ces analyses sont consignés dans le registre.</p>
  </li>

   
 <li>
   <h4>Mesures de Sécurité et de Confidentialité</h4>
  <p>Les mesures de sécurité et de confidentialité mises en place pour garantir la protection des données personnelles sont détaillées dans le registre. Cela inclut les mesures techniques et organisationnelles pour assurer la sécurité des données.</p>
  </li>
   
  <li><h4>Durées de Conservation des Données</h4>
  <p>Les durées de conservation des données ont été définies en conformité avec le RGPD. Le registre indique les périodes de conservation spécifiques pour chaque traitement de données.</p>
  </li>

</ol>

<h4>Responsabilités et Conformité au RGPD</h4>
<p>La mise à jour du registre des traitements de données personnelles est sous la responsabilité de <b>MR. NADIR Hicham</b>. L'ensemble de notre organisation est pleinement consciente de l'importance de se conformer au RGPD et de protéger les données personnelles des utilisateurs de Mastodon.</p>


























