# Projet d'exemple

Ce projet existe pour vérifier que votre environnement de développement local est bien configuré : vous avez besoin du kit de développement Java 17 ("JDK").

Vous pouvez compiler, lancer les tests, et lancer la méthode `main` avec le système de build Gradle.

Pas besoin de télécharger Gradle manuellement, le "wrapper" Gradle le fait pour vous :

```
# === Windows ===
# compiler + lancer les tests + obtenir la couverture de code
gradlew.bat build
# compiler + lancer la méthode `main`
gradlew.bat run

# === Linux / macOS (y.c. Windows Subsystem for Linux) ===
# même commentaires
./gradlew build
./gradlew run
```

Vous pouvez et devriez utilier votre environnement de développement préféré pour faire ces exercices, par exemple :
- Dans IntelliJ et Android Studio, choisissez "Ouvrir" et sélectionnez ce dossier
- Dans Eclipse, utilisez le menu Fichier >> Importer >> Gradle >> Projet Gradle existant, et sélectionnez ce dossier
