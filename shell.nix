{ lib, buildInputs ? [], ... }:
let
  pkgs = import <nixpkgs> {};
in
pkgs.mkShell {
  name = "whatsapp-bot-shell";
  buildInputs = buildInputs ++ [ pkgs.libgobject ];
}
