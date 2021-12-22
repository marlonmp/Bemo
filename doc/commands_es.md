# **Documentación de los comandos de Bemo** 🤖

A continuación, se presentan los comandos del Bot de música `Bemo`, con sus respectivos parámetros y explicación sencilla de su funcionamiento, estos comandos están divididos en tres secciones:

- **Comandos del canal de voz:** estos comandos arán que Bemo interactúe con los canales de audio, y los miembros del gremio de Discord.

- **Comandos de lista de música:** Estos comandos servirán para manejar la información de las listas de reproducción guardadas en caché.

- **Comandos de reproducción:** Estos comandos se encargarán de la reproducción de la música y las listas de reproducción.

## **Parámetros** 📑

- <a name=Id></a> **`Id`:** El parámetro `Id` es el identificador de una canción o de una lista de reproducción, el id mínimo posible es 1. su expresión regular de validación es: `^\d+$`.

- <a name=Title></a> **`Título`:** El parámetro `Título` hace referencia al título de la lista de reproducción, este parámetro solo puede contener letras de la `a` a la `z` en minúsculas, guion `-`, guion bajo `_` y números del `0` al `9`. El título solo puede contener entre `3` y `20` caracteres. Su expresión regular de validación es: `^[a-z\d\-\_]{3,20}$`.

- <a name=Prefix></a> **`Prefijo`:** El parámetro `Prefijo` es la id o las iniciales del título de la lista de reproducción (3 iniciales como mínimo). Sus expresiones regulares de validación son: `^\d+$` o `^[a-z\d\-\_]{3,20}$`.

- <a name=Url></a> **`Url`:** El parámetro `Url` hace referencia a la dirección (por el momento solo de Youtube) de la canción.

> **Nota:** En todos los comandos que se requiere los parámetros de la canción y la lista de reproducción, siempre irá primero la información de la lista de reproducción y luego la información de la canción.

**Comandos del canal de voz** 🔊
---

> - `!join` : Bemo entrará al canal de voz donde se aloje el emisor del comando.
> 
> - `!link` : Bemo seguiáa al usuario por los canales de voz.
>
> - `!unlink` : Bemo dejará de seguir al usuario enlazado.
>
> - `!leave` : Bemos saldrá del canal de voz donde esté.


**Comandos de música** 🎶
---

> - `!show` : Bemo listará todas las listas de reproducción en la caché.
>
> - `!list` [`Prefijo`](#Prefix) : Bemo listará las canciones que estén en la lista de reproducción seleccionada.
>
> - `!new` [`Título`](#Title) : Bemo creará una nueva lista de reproducción en caché, si el título no está en uso.
>
> - `!update` [`Prefijo`](#Prefix) [`Nuevo título`](#Title) : Bemo actualizará en caché el título de la lista de reproducción seleccionada.
>
> - `!delete` [`Id`](#Id) : Bemo eliminará de al caché la lista de reproducción seleccionada.
>   
> - `!add` [`Prefijo`](#Prefix) [`url`](#Url) : Bemo añadirá a la lista de reproducción en caché seleccionada la canción de la url.
>
> - `!remove` [`Prefijo`](#Prefix) [`Id`](#Id) : Bemo eliminará del a caché la canción de la lista de reproducción seleccionada.
>
> - `!save` : Bemo guardará en la base de datos la información que esté en caché.
    
**Comandos de reproducción** ⏯
---

> - `!start` [`Prefijo`](#Prefix) [`opcional[Id]`](#Id) : Si Bemo está en un canal de voz, iniciará la lista de reproducción con la primera canción, o la canción seleccionada.
>    
> - `!play` [`Id`](#Id) : Si Bemo está en un canal, y hay una lista de reproducción iniciada, reproducirá la canción indicada en el comando.
>
> - `!replay` : Si Bemo está en un canal, y hay una lista de reproducción iniciada, reiniciará la canción que está sonando.
>
> - `!next` : Si Bemo está en un canal, y hay una lista de reproducción iniciada, reproducirá la canción que sigue.  
>
> - `!previus` : Si Bemo está en un canal, y hay una lista de reproducción iniciada, reproducirá la canción anterior.
>
> - `!pause` : Si Bemo está en un canal, y hay una lista de reproducción iniciada, pausará la canción que está sonando.
>
> - `!resume` : Si Bemo está en un canal, y hay una lista de reproducción iniciada, y hay música pausada, la reanudará.
>
> - ~~`!loop`~~
>
> - `!shuffle` : Bemo revolverá la lista de reproducción iniciada.
  