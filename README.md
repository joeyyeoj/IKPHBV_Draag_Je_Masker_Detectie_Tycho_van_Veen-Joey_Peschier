# IKPHBV Eindopdracht :mask:


## Inleiding 
Voor de eindopdracht van IKPHBV moesten wij een mondkapjes-detectie met eigen toegevoegde functionaliteiten maken.
We hebben er voor gekozen om het programma na het detecteren van wel/geen mondkapje visueel en auditief feedback te laten geven aan de mensen die langs de camera lopen.

## Wat hebben we gedaan?
Allereerst hebben wij een geschikte mondkapjes detectie gezocht, na wat rondzoeken kwamen we uiteindelijk uit bij [deze Github repository](https://github.com/its-harshil/face-mask-detector/tree/master) <br>
Deze hebben wij overgenomen en allereerst werkend gemaakt op onze computers.


### Visuele feedback :eyes:
Als het programma heeft bepaald of de gebruiker wel of geen mondkapje op heeft, laat deze een van de onderstaande schermen zien:
Wel een mondkapje op       |  Geen mondkapje op
:-------------------------:|:-------------------------:
![](./Programma/groen.png)             |  ![](./Programma/rood.png)


Vervolgens leggen wij het frame met het gezicht van de gedetecteerde persoon over deze afbeelding heen, dit geheel laten we vervolgens zien in een window.

Wel een mondkapje op       |  Geen mondkapje op
:------------------------------------------------:|:------------------------------------------------:
![](./readme-afbeeldingen/groen_voorbeeld.png)      |  ![](./readme-afbeeldingen/rood_voorbeeld.png)  


### Auditieve feedback :ear:
Als het programma heeft bepaald of de gebruiker wel of geen mondapje op heeft, speelt deze een van de onderstaande geluidsfragmenten af:
<br>
* Als de gebruiker wel een mondkapje op heeft wordt [dit geluid](https://drive.google.com/file/d/1yFaovLgFu52kqvrA31P-WKFD5xyCLCua/view?usp=sharing) afgespeeld.
* Als de gebruiker geen mondkapje op heeft wordt [dit geluid](https://drive.google.com/file/d/18Kpk6sc696pDC5RA8c_lALSj8hmwShi0/view?usp=sharing) afgespeeld. <br>

Hiervoor hebben we de module [winsound](https://docs.python.org/3/library/winsound.html) gebruikt.


### Recovery
De recovery in het programma is heel degelijk, hij kan je gezicht vrij snel weer detecteren, wel gebeurt het soms dat het programma na het recoveren vastloopt omdat het te veel inputs ontvangt.

### Performance in het donker
Wel een mondkapje op       |  Geen mondkapje op
:------------------------------------------------:|:------------------------------------------------:
![](./readme-afbeeldingen/donker_voorbeeld.png)      |  ![](./readme-afbeeldingen/donker_voorbeeld_rood.png)  

Zoals hier boven te zien doet het programma het best heel redelijk in het donker, de detectie van het mondkapje werkt nog goed, en ook mijn gezicht word nog goed gedetecteerd.

### Andere kleuren mondkapjes
De dataset die we hebben gebruikt bestaat uit foto's waar met de computer een mondkapje over heen is geplakt, dit zijn altijd witte mondkapjes, hierdoor is het programma slecht in het detecteren van bijvoorbeeld een zwart mondkapje. Dit zou opgelost kunnen worden door een aantal zwarte mondkapjes toe te voegen in de dataset, maar de maker van het programma gaf aan dat dit problemen oplevert wanneer het probeert een mondkapje te detecteren op iemand met een baard.



## Uitdagingen :muscle:
De uitdagingen lagen vooral bij het afspelen van het geluid op een redelijke manier, mede omdat we eerst de module [playsound](https://pypi.org/project/playsound/) wilde gebruiken, het afspelen met deze module is erg makkelijk maar helaas leverde dit wat problemen op, zo speelde het geluid zichzelf tijdens elke frame die het programma detecteerde opnieuw af, ook hadden we met deze module het probleem dat geluiden tegelijk af werden gespeeld, waardoor iemand die door het scherm toch zijn mondkapje op heeft gezet door het applaus heen nog steeds een negatief geluid kreeg te horen.<br><br>
Uiteindelijk zijn we overgestapt op winsound, deze module heeft wat meer mogelijkheden betreft het afspelen van een geluid, zo kan er worden gekozen om de flag 'SND_ASYNC' aan te zetten, dit zorgt er voor dat het programma niet hoeft te wachten tot het audiobestand helemaal is afgespeeld. <br><br>
Hiermee was het probleem van het bestand dat meerdere keren werd afgespeeld en het probleem van de geluiden die door elkaar werden afgespeeld opgelost, maar helaas wisten wij niet dat winsound alleen .wav bestanden af kan spelen, na een aantal pogingen met een .mp3 bestand zijn we hier toch achter gekomen en hebben we onze .mp3 bestanden omgezet naar .wav om dit te laten werken.



## Bronnen :bookmark_tabs:
* [Github repo](https://github.com/its-harshil/face-mask-detector/tree/master)
* [winsound](https://docs.python.org/3/library/winsound.html)

## Auteurs
Tycho van Veen (s1122689)<br>
Joey Peschier (s1120743)
