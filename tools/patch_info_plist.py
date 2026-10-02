#!/usr/bin/env python3
"""Patch an extracted NB.app Info.plist to register .NullsBrawlAssets with iOS."""

from pathlib import Path
import plistlib

PLIST = Path("Payload/NB.app/Info.plist")

with PLIST.open("rb") as f:
    p = plistlib.load(f)

ut = {
    "UTTypeIdentifier": "com.nullsbrawl.assets",
    "UTTypeDescription": "Null's Brawl Assets",
    "UTTypeConformsTo": ["public.data", "public.content"],
    "UTTypeTagSpecification": {
        "public.filename-extension": ["NullsBrawlAssets"]
    },
}

p["UTExportedTypeDeclarations"] = [
    x for x in p.get("UTExportedTypeDeclarations", [])
    if x.get("UTTypeIdentifier") != "com.nullsbrawl.assets"
] + [ut]

doc = {
    "CFBundleTypeName": "Null's Brawl Assets",
    "CFBundleTypeRole": "Editor",
    "LSHandlerRank": "Owner",
    "LSItemContentTypes": ["com.nullsbrawl.assets"],
}

p["CFBundleDocumentTypes"] = [
    x for x in p.get("CFBundleDocumentTypes", [])
    if "com.nullsbrawl.assets" not in x.get("LSItemContentTypes", [])
] + [doc]

with PLIST.open("wb") as f:
    plistlib.dump(p, f, fmt=plistlib.FMT_BINARY, sort_keys=False)

print("Patched:", PLIST)
