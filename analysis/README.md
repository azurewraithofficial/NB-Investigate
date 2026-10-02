# Null's Brawl IPA investigation

IPA: nb_69.252_4cc76283.ipa
Bundle: nt.nb.ios
Version: 69.252

## Finding

The app's Payload/NB.app/Info.plist does not contain:
- CFBundleDocumentTypes
- UTExportedTypeDeclarations
- UTImportedTypeDeclarations
- LSItemContentTypes

No .NullsBrawlAssets registration was found in the plist/resource metadata inspected.

The bundle also contains no .appex application extensions.

## Important limitation

The IPA contains compiled native code, not the original source code. The original source cannot be reconstructed faithfully from the IPA. This repository therefore stores the reproducible investigation and a metadata patch rather than pretending the binary is source code.

Changing Info.plist changes the signed app bundle and will invalidate the original iOS code signature. A legitimately re-signed build is required for installation/testing.

## Patch goal

Register .NullsBrawlAssets with Launch Services/Uniform Type Identifiers so iOS can associate the file with the app. This does not prove that the compiled app contains an importer for the file format.
