{ jacobi ? import
    (fetchTarball {
      name = "jacobi-2022-12-02";
      url = "https://nix.cobi.dev/x/af0b49506699c45d7ff6cd98d7e12df9c9394735";
      sha256 = "14nhzxby34jaay0ig9hgm4n31255am0zbixp63dsxc5515gki8sa";
    })
    { }
}:
let
  name = "advent2022";


  tools = with jacobi; {
    cli = [
      jq
      nixpkgs-fmt
    ];
    python = [
      (python310.withPackages (p: with p; [
        requests
        typing
      ]))
    ];
  };

  env = jacobi.enviro {
    inherit name tools;
  };
in
env
