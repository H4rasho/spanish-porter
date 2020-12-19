PUNTOS ="\p{Punct}"
SIMBOLOS = "([^(\\s)ñ(\\w)]|)"
TILDE_A="[áàä]"
TILDE_E="[éèë]"
TILDE_I="[íìï]"
TILDE_O="[óòö]"
TILDE_U="[úùü]"
ESPACIO="\\b"
ALFABETO ="(a-z)"
ALFABETO_SUFIJOS ="[a-z]"
DIGITOS ="\\d"
#prefijos
PREFIJO1 =ESPACIO+"a[n*]?"+ALFABETO+"*"
PREFIJO2 =ESPACIO+"bi[s*]?"+ALFABETO+"*"
PREFIJO3 =ESPACIO+"ant[ei]"+ALFABETO+"*"
PREFIJO4 =ESPACIO+"co[n*]?"+ALFABETO+"*"
PREFIJO5 =ESPACIO+"en"+ALFABETO+"*"
PREFIJO6 =ESPACIO+"entre?"+ALFABETO+"*"
PREFIJO7 =ESPACIO+"(extra)"+ALFABETO+"*"
PREFIJO8 =ESPACIO+"(ex)"+ALFABETO+"*"
PREFIJO9 =ESPACIO+"hip(er)"+ALFABETO+"*"
PREFIJO10 =ESPACIO+"pos(t*)"+ALFABETO+"*"
PREFIJO11 =ESPACIO+"(p*)re"+ALFABETO+"*"
PREFIJO12 =ESPACIO+"sub"+ALFABETO+"*"
PREFIJO13 =ESPACIO+"super"+ALFABETO+"*"
PREFIJO14 =ESPACIO+"hip(o)"+ALFABETO+"*"
#adjetivos
ADJETIVO1 =ALFABETO_SUFIJOS+"([ai]ble)"+ESPACIO
ADJETIVO2 =ALFABETO_SUFIJOS+"([ai]do)"+ESPACIO
ADJETIVO3 =ALFABETO_SUFIJOS+"([ia]no)"+ESPACIO
ADJETIVO4 =ALFABETO_SUFIJOS+"(a[lr])"+ESPACIO
ADJETIVO5 =ALFABETO_SUFIJOS+"(ense)"+ESPACIO
ADJETIVO6 =ALFABETO_SUFIJOS+"(eño)"+ESPACIO
ADJETIVO7 =ALFABETO_SUFIJOS+"(iento)"+ESPACIO
ADJETIVO8 =ALFABETO_SUFIJOS+"(il)"+ESPACIO
ADJETIVO9 =ALFABETO_SUFIJOS+"(i[nz]o)"+ESPACIO
ADJETIVO10 =ALFABETO_SUFIJOS+"(oso)"+ESPACIO
ADJETIVO11 =ALFABETO_SUFIJOS+"(udo)"+ESPACIO
#subfijos de sustantivos
SUSTANTIVO1 =ALFABETO_SUFIJOS+"(aje)"+ESPACIO
SUSTANTIVO2 =ALFABETO_SUFIJOS+"([ae]ncia)"+ESPACIO
SUSTANTIVO3 =ALFABETO_SUFIJOS+"(ante)"+ESPACIO
SUSTANTIVO4 =ALFABETO_SUFIJOS+"(a[lr])"+ESPACIO
SUSTANTIVO5 =ALFABETO_SUFIJOS+"(ario)"+ESPACIO
SUSTANTIVO6 =ALFABETO_SUFIJOS+"(dad)"+ESPACIO
SUSTANTIVO7 =ALFABETO_SUFIJOS+"(eria)"+ESPACIO
SUSTANTIVO8 =ALFABETO_SUFIJOS+"(ero)"+ESPACIO
SUSTANTIVO9 =ALFABETO_SUFIJOS+"(ez)"+ESPACIO
SUSTANTIVO10 =ALFABETO_SUFIJOS+"(ista)"+ESPACIO
SUSTANTIVO11 =ALFABETO_SUFIJOS+"(ura)"+ESPACIO
#subfijos de aumentativos
AUMENTATIVO1 =ALFABETO_SUFIJOS+"(azo)"+ESPACIO
AUMENTATIVO2 =ALFABETO_SUFIJOS+"(on)"+ESPACIO
AUMENTATIVO3 =ALFABETO_SUFIJOS+"(ote)"+ESPACIO
#subfijos de disminutivos
DISMINUTIVO1 =ALFABETO_SUFIJOS+"([cz]?i[ct][oa])"+ESPACIO
DISMINUTIVO2 =ALFABETO_SUFIJOS+"([cz]?illo)"+ESPACIO
DISMINUTIVO3 =ALFABETO_SUFIJOS+"([cz]?in)"+ESPACIO
DISMINUTIVO4 =ALFABETO_SUFIJOS+"([cz]?uelo)"+ESPACIO
#sufijos despectivos
DESPECTIVO1 =ALFABETO_SUFIJOS+"(acho)"+ESPACIO
DESPECTIVO2 =ALFABETO_SUFIJOS+"(aco)"+ESPACIO
DESPECTIVO3 =ALFABETO_SUFIJOS+"(ajo)"+ESPACIO
DESPECTIVO4 =ALFABETO_SUFIJOS+"(astro)"+ESPACIO
DESPECTIVO5 =ALFABETO_SUFIJOS+"(ucho)"+ESPACIO
#subfijos de verbos
VERBO1 =ALFABETO_SUFIJOS+"(ear)"+ESPACIO
VERBO2 =ALFABETO_SUFIJOS+"(ecer)"+ESPACIO
VERBO3 =ALFABETO_SUFIJOS+"(ificar)"+ESPACIO
VERBO4 =ALFABETO_SUFIJOS+"(izar)"+ESPACIO
#articulos
ARTICULO1 =ESPACIO+"(e[nl])"+ESPACIO
ARTICULO2 =ESPACIO+"(la(s?))"+ESPACIO
ARTICULO3 =ESPACIO+"(lo(s?))"+ESPACIO
ARTICULO4 =ESPACIO+"(un)"+ESPACIO
ARTICULO5 =ESPACIO+"(unas)"+ESPACIO
ARTICULO6 =ESPACIO+"(unos)"+ESPACIO
ARTICULO7 =ESPACIO+"(una)"+ESPACIO
#pronombres
PRONOMBRE1 =ESPACIO+"est([ea?]s?)"+ESPACIO
PRONOMBRE2 =ESPACIO+"esto"+ESPACIO
PRONOMBRE3 =ESPACIO+"es([oa?]s?)"+ESPACIO
PRONOMBRE4 =ESPACIO+"es"+ESPACIO
PRONOMBRE5 =ESPACIO+"aquell[oa]s?"+ESPACIO
PRONOMBRE6 =ESPACIO+"aquel"+ESPACIO
PRONOMBRE7 =ESPACIO+"[vn?]uestr[ao?]s?"+ESPACIO
PRONOMBRE8 =ESPACIO+"mi[oa?]s?"+ESPACIO
PRONOMBRE9 =ESPACIO+"un[ao]s?"+ESPACIO
PRONOMBRE10 =ESPACIO+"dos"+ESPACIO
PRONOMBRE11 =ESPACIO+"tres"+ESPACIO
PRONOMBRE12 =ESPACIO+"cuatro"+ESPACIO
PRONOMBRE13 =ESPACIO+"tercer[ao]?s?"+ESPACIO
PRONOMBRE14 =ESPACIO+"primer[ao]?s?"+ESPACIO
PRONOMBRE15 =ESPACIO+"segund[ao]s?"+ESPACIO
PRONOMBRE16 =ESPACIO+"(ningun)[oa]?s?"+ESPACIO
PRONOMBRE17 =ESPACIO+"(algun)[oa]?s?"+ESPACIO
PRONOMBRE18 =ESPACIO+"(un)[oa]?s?"+ESPACIO
PRONOMBRE19 =ESPACIO+"otr[ao]s?"+ESPACIO
PRONOMBRE20 =ESPACIO+"poc[ao]s?"+ESPACIO
PRONOMBRE21 =ESPACIO+"tod[ao]s?"+ESPACIO
PRONOMBRE22 =ESPACIO+"much[ao]s?"+ESPACIO
PRONOMBRE23 =ESPACIO+"vari[oa]s"+ESPACIO
PRONOMBRE24 =ESPACIO+"para"+ESPACIO
PRONOMBRE25 =ESPACIO+"nadie"+ESPACIO
PRONOMBRE26 =ESPACIO+"nada"+ESPACIO
PRONOMBRE27 =ESPACIO+"algo"+ESPACIO
PRONOMBRE28 =ESPACIO+"alguien"+ESPACIO
PRONOMBRE29 =ESPACIO+"bastantes?"+ESPACIO
PRONOMBRE30 =ESPACIO+"yo"+ESPACIO
PRONOMBRE31 =ESPACIO+"m[ei]"+ESPACIO
PRONOMBRE32 =ESPACIO+"con[ms]igo"+ESPACIO
PRONOMBRE33 =ESPACIO+"(vosotr)[ao]s"+ESPACIO
PRONOMBRE34 =ESPACIO+"(nosotr)[ao]s"+ESPACIO
PRONOMBRE35 =ESPACIO+"t[uei]"+ESPACIO
PRONOMBRE36 =ESPACIO+"ell[ao]s?"+ESPACIO
PRONOMBRE37 =ESPACIO+"el"+ESPACIO
PRONOMBRE38 =ESPACIO+"s[ei]"+ESPACIO
PRONOMBRE39 =ESPACIO+"l[aoe]s?"+ESPACIO
PRONOMBRE40 =ESPACIO+"[ts]uy[oa]s?"+ESPACIO

