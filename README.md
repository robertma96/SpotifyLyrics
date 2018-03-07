# SpotifyLyrics
Versuri pentru melodiile ascultate in Spotify. 

Functioneaza doar pe varianta de aplicatie in Windows. Ceea ce face este sa procure numele si artistul melodiei, iar dupa aceea va face un request in baza acestor 2 campuri la www.azlyrics.com

Exemplu 
Artist Name: Imagine Dragons
Song Name: Believer
Request-ul va fi facut la https://www.azlyrics.com/lyrics/imaginedragons/believer.html, de unde sunt extrase versurile si afisate in consola. Nu i-am creat GUI, deoarece nu mi s-a parut impedios necesar pentru ce imi trebuia.

Am facut acest script deoarece la multe melodii imi doream sa aflu versurile, fara a mai intra pe google. Script-ul este foarte dependent de forma campurilor artist name si song name, de aceea nu functioneaza la toate piesele, unele nici un existand pe www.azilyrics.com. Initial am dorit sa folosesc un API pentru a face rost de aceste versuri, dar lucrurile deveneau complicate (anumite API-uri cereau remuneratie), asa ca am optat pentru azlyrics.

Pentru a verifica functionalitatea script-ului, mai intai se deschide aplicatia de Spotify, apoi se ruleaza script-ul.
