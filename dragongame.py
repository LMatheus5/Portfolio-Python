print('''

                        /\
                        ||
                        ||
                        ||
                        ||                                               ~-----~
                        ||                                            /===--  ---~~~
                        ||                   ;'                 /==~- --   -    ---~~~
                        ||                (/ ('              /=----         ~~_  --(  '
                        ||             ' / ;'             /=----               \__~
     '                ~==_=~          '('             ~-~~      ~~~~        ~~~--\~'
     \\                (c_\_        .i.             /~--    ~~~--   -~     (     '
      `\               (}| /       / : \           / ~~------~     ~~\   (
      \ '               ||/ \      |===|          /~/             ~~~ \ \(
      ``~\              ~~\  )~.~_ >._.< _~-~     |`_          ~~-~     )\
       '-~                 {  /  ) \___/ (   \   |` ` _       ~~         '
       \ -~\                -<__/  -   -  L~ -;   \\    \ _ _/
       `` ~~=\                  {    :    }\ ,\    ||   _ :(
        \  ~~=\__                \ _/ \_ /  )  } _//   ( `|'
        ``    , ~\--~=\           \     /  / _/ / '    (   '
         \`    } ~ ~~ -~=\   _~_  / \ / \ )^ ( // :_  / '
         |    ,          _~-'   '~~__-_  / - |/     \ (
          \  ,_--_     _/              \_'---', -~ .   \
           )/      /\ / /\   ,~,         \__ _}     \_  "~_
           ,      { ( _ )'} ~ - \_    ~\  (-:-)       "\   ~ 
                  /'' ''  )~ \~_ ~\   )->  \ :|    _,       " 
                 (\  _/)''} | \~_ ~  /~(   | :)   /          }
                <``  >;,,/  )= \~__ {{{ '  \ =(  ,   ,       ;
               {o_o }_/     |v  '~__  _    )-v|  "  :       ,"
               {/"\_)       {_/'  \~__ ~\_ \\_} '  {        /~\
               ,/!          '_/    '~__ _-~ \_' :  '      ,"  ~ 
              (''`                  /,'~___~    | /     ,"  \ ~' 
             '/, )                 (-)  '~____~";     ,"     , }
           /,')                    / \         /  ,~-"       '~'
       (  ''/                     / ( '       /  /          '~'
    ~ ~  ,, /) ,                 (/( \)      ( -)          /~'
  (  ~~ )`  ~}                   '  \)'     _/ /           ~'
 { |) /`,--.(  }'                    '     (  /          /~'
(` ~ ( c|~~| `}   )                        '/:\         ,'
 ~ )/``) )) '|),                          (/ | \)                 -sjm
  (` (-~(( `~`'  )                        ' (/ '
   `~'    )'`')                              '
     ` ``
''')

print("Bem vindo à Ilha do Dragão.")
print("A sua missão é entrar no castelo e encontrar o tesouro do Dragão.")
entry = input("Vamos começar? Digite [Y] para começar ou [N] para encerrrar o jogo.").lower()
if entry == "y":
    print("Temos um aventureiro corajoso aqui não é mesmo!?")
    escolha1 = input("Entrando no castelo, você se depara com um caminho a esquerda e um a direita, por qual você quer seguir?[E] ou [D]").lower()
    if escolha1 == "e":
        print("Você avança pelo castelo.")
        escolha2 = input("Logo a frente você encontra uma ponte que dá acesso a uma torre interna no castelo.A ponte é guardada por um cavaleiro de armadura negra, portando uma Claymore.[S] para subornar o guarda ou [E] para esperar.").lower()
        if escolha2 == "e":
            print("Você espera alguns minutos e o guarda vai fazer a sua patrulha, se distanciando cada vez mais da ponte.")
            escolha3 = input("Você adentra na torre, uma grande sala com duas portas, uma vermelha outra preta. Escolha [V] para vermelha ou [P] para preta.").lower()
            if escolha3 == "v":
                print("Parabens você encontrou o tesouro...")
                print("Um enorme dragão vermelho fecha a porta atrás de você com a batida de suas asas e diz: Venha pequeno camundongo, tente pegar meu ouro.")
            else:
                print("Você adentra na sala dos guardas, onde estão 4 guardas armados e equipados. Seu final não é feliz.")
        else:
            print("A ultima coisa que você escuta é o guarda dizer: Seu ouro é insignificante aqui! Apos isso uma enorme escuridão recai sobre você.")
    else:
        print("Você dá de cara com guardas do castelo, seu final é trágico.")

else:
    print("Temos um aventureiro que preza por sua vida, Adeus.")







