# KryptosED

![Icona de l'Aplicació](utils/images/icon.png)

## Català

## Visió General

**KryptosED** és una eina fàcil d'utilitzar per a xifrar i desxifrar fitxers i carpetes, dissenyada amb una interfície moderna utilitzant `customtkinter`. Aquesta aplicació proporciona xifratge AES-256 robust amb una barra de progrés en temps real, permetent-vos monitoritzar les operacions de xifratge/desxifratge. Tant si voleu protegir les vostres dades sensibles, experimentar amb criptografia o personalitzar el vostre espai de treball, aquesta aplicació combina seguretat amb característiques amigables per a l'usuari.

---

## Per què Utilitzar Aquesta Aplicació?

- **Seguretat de Grau Militar:** Utilitza xifratge AES-256, el mateix estàndard en què confien governs i experts en seguretat a tot el món.
- **Seguiment de Progrés en Temps Real:** Monitoritza les operacions de xifratge/desxifratge amb una barra de progrés visual que s'actualitza a mesura que es processen els fitxers.
- **Protegir les Dades:** Xifra fàcilment informació sensible per mantenir-la privada d'accés no autoritzat.
- **Aprendre sobre Xifratge:** Perfecta per a estudiants i entusiastes per entendre conceptes de xifratge modern.
- **Personalitzar Tot:** Canvia tipus de lletra, colors i imatges per fer l'aplicació veritablement teva.
- **Vista Prèvia de Tipus de Lletra:** Viu instantàniament com es veuen diferents tipus de lletra abans d'aplicar-los.

---

## Característiques

- **Xifratge/Desxifratge de Fitxers AES-256:**  
  Xifra o desxifra fitxers amb mode AES-256-CTR, un dels estàndards de xifratge més segurs disponibles. Cada xifratge genera una clau criptogràfica única per a màxima seguretat.

- **Visualització de Progrés en Temps Real:**  
  Observa el progrés del xifratge/desxifratge amb una barra de progrés dinàmica que s'actualitza a mesura que es processa cada bloc de 64KB.

- **Gestió Segura de Claus:**  
  Les claus de xifratge es generen de forma segura i es guarden com a fitxers binaris. Opció per eliminar automàticament les claus després d'un desxifratge exitós.

- **Interfície Moderna i Personalitzable:**  
  Construïda amb `customtkinter` per a una interfície elegant i moderna amb fàcil personalització d'aparença.

- **Utilitat de Vista Prèvia de Tipus de Lletra:**  
  Utilitza `test_fonts.py` per previsualitzar i seleccionar entre una àmplia gamma de tipus de lletra abans d'implementar-los en l'aplicació principal.

- **Suport per a Imatges i Icones:**  
  Canvia fàcilment imatges i icones per personalitzar la teva experiència.

- **Suport per a Múltiples Fitxers via Compressió:**  
  Xifra múltiples fitxers comprimint-los primer en un sol arxiu, després xifrant l'arxiu com un únic fitxer segur.

---

## Començant

### 1. Instal·lació

Assegura't de tenir Python 3.7+ instal·lat. Després, instal·la les llibreries requerides:

```bash
pip install -r requirements.txt
```

**Llibreries Requerides:**
- `PyCryptodome` - Per a implementació de xifratge AES-256
- `customtkinter` - Per a components d'interfície moderna
- `tkinter` - Per a elements GUI i barres de progrés
- `Pillow` - Per a manipulació i suport d'imatges

### 2. Executant l'Aplicació

Executa el paquet Python:

```bash
python -m KryptosED
```

### 3. Xifrant Fitxers

1. Fes clic a "Xifrar Fitxer" a la interfície principal
2. Selecciona el fitxer que vols xifrar
3. Apareixerà una barra de progrés mostrant el progrés del xifratge en temps real
4. Després de completar el xifratge, tria una ubicació per guardar la teva clau de xifratge
5. El fitxer xifrat ara reemplaça l'original (¡guarda el fitxer de clau de forma segura per al desxifratge!)

### 4. Desxifrant Fitxers

1. Fes clic a "Desxifrar Fitxer" a la interfície principal
2. Selecciona el fitxer xifrat
3. Selecciona el fitxer `.key.bin` corresponent
4. Observa la barra de progrés mentre el teu fitxer es desxifra
5. Tria si vols mantenir o eliminar el fitxer de clau després del desxifratge

### 5. Múltiples Fitxers (Compressió)

Per xifrar o desxifrar diversos fitxers alhora, utilitza la funció de compressió de l'aplicació:
1. Selecciona múltiples fitxers o una carpeta que contingui els teus fitxers.
2. L'aplicació els comprimirà automàticament en un sol arxiu (ex. ZIP).
3. L'arxiu comprimit es xifra o desxifra com a únic fitxer amb seguiment de progrés.
4. Després del desxifratge, l'arxiu comprimit pot extreure's per restaurar els fitxers originals.

*Això és útil per a manejar de forma segura lots de fitxers i mantenir tot organitzat.*

---

## Detalls Tècnics

### Mètode de Xifratge
- **Algorisme:** AES-256 (Estàndard de Xifratge Avançat amb clau de 256 bits)
- **Mode:** CTR (Mode Comptador) - Proporciona seguretat semàntica i processament paral·lel
- **Generació de Clau:** Generació de clau aleatòria criptogràficament segura (32 bytes)
- **Nonce:** Nonce aleatori de 8 bytes per a mode CTR, emmagatzemat amb el fitxer xifrat

### Característiques de Seguretat
- Cada operació de xifratge genera una clau única i aleatòria
- Les claus mai s'emmagatzemen amb les dades xifrades
- Sense reutilització de contrasenyes - cada fitxer obté la seva pròpia clau criptogràfica
- La barra de progrés no compromet la seguretat - només mostra l'estat del processament

### Rendiment
- Processa fitxers en blocs de 64KB per a eficiència de memòria
- Actualitzacions de progrés en temps real durant el processament
- Suporta fitxers de qualsevol mida
- Sobrecàrrega mínima de rendiment per a xifratge fort

---

## Personalitzant l'Aplicació

### Tipus de Lletra

- Obre `src/operation/utils/test_fonts.py` i executa'l:
  ```bash
  python src/operation/utils/test_fonts.py
  ```
- Navega per les mostres de tipus de lletra.  
- Aplica el teu tipus de lletra escollit a l'aplicació principal actualitzant la secció de codi rellevant (veure comentaris al codi).

### Imatges

- Afegeix els teus fitxers d'imatge a /images i canvia el seu nom a `icon.png`.
- Actualitza les rutes de les imatges al codi a la variable `title_letter` i `font_letter` a `main.py`.
- Reinicia l'aplicació per veure els teus canvis.

### Colors i Estils

- Modifica els paràmetres de color i estil al codi (cerca configuracions de `customtkinter`).
- Experimenta amb diferents temes i dissenys.

### Personalització de la Barra de Progrés
La barra de progrés pot personalitzar-se a `encryption.py` i `decryption.py`:
- Canvia la mida del bloc per a diferents característiques de rendiment
- Modifica l'aparença de la barra de progrés (color, longitud, estil)
- Afegeix etiquetes de percentatge o estimacions de temps

---

## Compilant a un Executable (.exe)

Vols compartir la teva aplicació com un executable independent per a Windows?

1. Instal·la PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Compila la teva aplicació:
   ```bash
   pyinstaller --onefile --windowed --name KryptosED --icon=KryptosED/utils/images/icon.png --add-data "KryptosED/utils/images/icon.png;KryptosED/utils/images" KryptosED/__main__.py
   ```
3. Troba el teu `.exe` a la carpeta `dist`.

**Nota:**  
PyInstaller empaqueta automàticament totes les dependències requerides del teu entorn Python a l'executable. No necessites instal·lar dependències per separat a la màquina destí.

---

## Millors Pràctiques de Seguretat

1. **Sempre fes còpia de seguretat de les teves claus de xifratge** - Sense la clau, els fitxers xifrats són irrecuperables
2. **Emmagatzema les claus separades de les dades xifrades** - Mai les mantinguis a la mateixa ubicació
3. **Utilitza contrasenyes fortes** per al teu sistema on s'emmagatzemen les claus
4. **Elimina les claus de forma segura** després d'usar-les si ja no necessites accés a les dades
5. **Verifica la integritat del fitxer** després del desxifratge comprovant mides i extensions de fitxer

---

## Solució de Problemes

- **"ModuleNotFoundError: No module named 'Crypto'"**  
  Instal·la PyCryptodome: `pip install pycryptodome`

- **La barra de progrés no s'actualitza**  
  Assegura't que estàs executant la versió més recent amb els mòduls de xifratge/desxifratge actualitzats

- **El desxifratge falla**  
  Verifica que estiguis utilitzant el fitxer de clau correcte per al fitxer xifrat. Cada clau és única per al seu fitxer.

- **Els fitxers grans triguen temps**  
  Això és normal - AES-256 està processant cada byte del teu fitxer per a màxima seguretat

---

## Crèdits

- Desenvolupat per **v0id0100**
- Utilitza la llibreria **PyCryptodome** per a implementació AES-256
- Construït amb **customtkinter** per a components GUI moderns
- Implementació de barra de progrés utilitzant **tkinter.ttk**

---

## Historial de Versions

### v1.1.0
- Afegides barres de progrés en temps real per a xifratge/desxifratge
- Implementació millorada de AES-256-CTR
- Interfície de gestió de claus millorada
- Millor maneig d'errors i retroalimentació a l'usuari

### v1.0.0
- Llançament inicial amb xifratge/desxifratge bàsic
- Interfície personalitzable amb vista prèvia de tipus de lletra
- Suport de compressió de fitxers per a operacions per lots

---

**Descàrrec de responsabilitat:** Aquesta eina és per a ús educatiu i personal. Els desenvolupadors no són responsables de cap pèrdua de dades o violacions de seguretat resultants de l'ús incorrecte d'aquest programari. Sempre mantén còpies de seguretat de dades importants abans d'operacions de xifratge.