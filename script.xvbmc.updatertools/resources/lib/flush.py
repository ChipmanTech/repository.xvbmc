exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("IyEvZWMvYmQvMTBlCiIiIzA6Ngo0YSAxMGEgYjcgMTNmICxlZSBiNyBjNSAsOGQgYjcgZTggLDdlIGI3IDVkICMwOjI1CjRhIGE1IGI3IDUgLDcxIGI3IDVlICMwOjI2CjRhIDEwYyBiNyBjICMwOjI3CjZjID0nMTBkLjliLmQ0JyMwOjM1CjlkID1jNSAuOWMgKDEzYyA9NmMgKSMwOjM2CjFkID1lOCAuYWEgKCkjMDozOAoxMSA9ImMzIGI0IiMwOjM5CjFmIGIyICgpOiMwOjQxCgkiIiMwOjQyCgkxID1bXSMwOjQ0CgkxIC4xYiAoIjEyIFtiXTExY1svYl0gMTcgLSAyMSBkNyIpIzA6NDUKCTEgLjFiICgiMTIgW2JdMTFjWy9iXSAxNyAtIDEzNCBkYiIpIzA6NDYKCTEgLjFiICgiMTIgW2JdNWZbL2JdIDE3IC0gMjEgZDciKSMwOjQ3CgkxIC4xYiAoIjEyIFtiXTVmWy9iXSAxNyAtIDEzNCBkYiIpIzA6NDgKCTEgLjFiICgiMWMgLSAyMSBkNyIpIzA6NDkKCTEgLjFiICgiMWMgLSAyMSAxMWIiKSMwOjUwCgkxIC4xYiAoIltkIDc0XWZlWy9kXSBbZCAxMDldYjBbL2RdIFtkIDc0XTdmIDVhICg5MSAxMTQpWy9kXSBbZCA2OF1bYTNdW2JdXCdbL2JdN2IgZTZbYl1cJ1svYl1bL2EzXVsvZF0iKSMwOjUxCgkxIC4xYiAoIltiXVtkIDdjXWExWy9kXVsvYl0iKSMwOjUyCgk5ID1lOCAuYWEgKCkuOTggKDExICsiIFtiXS1bL2JdIGFiIDlhIGQ3LzhhIiwxICkjMDo1NQoJNWIgMSBbOSBdPT0iMTIgW2JdMTFjWy9iXSAxNyAtIDIxIGQ3IjojMDo1NwoJCTZhICgpIzA6NTgKCTI4IDEgWzkgXT09IjEyIFtiXTExY1svYl0gMTcgLSAxMzQgZGIiOiMwOjYwCgkJNmQgKCkjMDo2MQoJMjggMSBbOSBdPT0iMTIgW2JdNWZbL2JdIDE3IC0gMjEgZDciOiMwOjYzCgkJNmYgKCkjMDo2NAoJMjggMSBbOSBdPT0iMTIgW2JdNWZbL2JdIDE3IC0gMTM0IGRiIjojMDo2NgoJCTZiICgpIzA6NjcKCTI4IDEgWzkgXT09IjFjIC0gMjEgZDciOiMwOjY5CgkJNTQgKCkjMDo3MAoJMjggMSBbOSBdPT0iMWMgLSAyMSAxMWIiOiMwOjcyCgkJMTJiICgpIzA6NzMKCTI4IDEgWzkgXT09IltkIDc0XWZlWy9kXSBbZCAxMDldYjBbL2RdIFtkIDc0XTdmIDVhICg5MSAxMTQpWy9kXSBbZCA2OF1bYTNdW2JdXCdbL2JdN2IgZTZbYl1cJ1svYl1bL2EzXVsvZF0iOiMwOjc1CgkJZDMgKCkjMDo3NgoyZSA0ZCAoZTggLjI0ICk6IzA6NzgKICAxZiAxOSAoMTJlICk6IzA6NzkKCTM0ID01IC5mIC4yOSAoMTNmIC5hICg1IC5mIC4xOCAoJzE0Oi8vZGQnLCcyYicsJzNkLjEzLjJmLmFjJykpKSMwOjgwCgk1YiAzNCA6MTNmIC4xMCAoIjFlKDNkOi8vM2QuMTMuMmYuYWMvPzExZT01MykiKSMwOjgxCglhZCA6IzA6ODIKCQkxZCAuMTFmICgxMSAsJzEyIDExYyAxNyAyMiA0YyA0ZSA3NyBjNiAyMycsJycsJyguLi4xMiAxMWMgMTcgNTkgMTJkLi4uKScpIzA6ODMKMmUgYWYgKGU4IC4yNCApOiMwOjg1CiAgMWYgMTkgKDEyZSApOiMwOjg2CgkzNyA9NSAuZiAuMjkgKDEzZiAuYSAoNSAuZiAuMTggKCcxNDovL2RkJywnMmInLCczZC4xMy4yZi5hYycpKSkjMDo4NwoJNWIgMzcgOjEzZiAuMTAgKCIxZSgzZDovLzNkLjEzLjJmLmFjLz8xMWU9NjIpIikjMDo4OAoJYWQgOiMwOjg5CgkJMWQgLjExZiAoMTEgLCcxMiAxMWMgMTcgMjIgNGMgNGUgNzcgYzYgMjMnLCcnLCcoLi4uMTIgMTFjIDE3IDU5IDEyZC4uLiknKSMwOjkwCjJlIDRiIChlOCAuMjQgKTojMDo5MgogIDFmIDE5ICgxMmUgKTojMDo5MwoJMzMgPTUgLmYgLjI5ICgxM2YgLmEgKDUgLmYgLjE4ICgnMTQ6Ly9kZCcsJzJiJywnM2QuMTMuMmQuYWMnKSkpIzA6OTQKCTViIDMzIDoxM2YgLjEwICgiMWUoM2Q6Ly8zZC4xMy4yZC5hYy8/MTFlPTUzKSIpIzA6OTUKCWFkIDojMDo5NgoJCTFkIC4xMWYgKDExICwnMTIgNWYgMTcgMjIgNGMgNGUgNzcgYzYgMjMnLCcnLCcoLi4uMTIgNWYgMTcgNTkgMTJkLi4uKScpIzA6OTcKMmUgNGYgKGU4IC4yNCApOiMwOjk5CiAgMWYgMTkgKDEyZSApOiMwOjEwMAoJYzQgPTUgLmYgLjI5ICgxM2YgLmEgKDUgLmYgLjE4ICgnMTQ6Ly9kZCcsJzJiJywnM2QuMTMuMmQuYWMnKSkpIzA6MTAxCgk1YiBjNCA6MTNmIC4xMCAoIjFlKDNkOi8vM2QuMTMuMmQuYWMvPzExZT02MikiKSMwOjEwMgoJYWQgOiMwOjEwMwoJCTFkIC4xMWYgKDExICwnMTIgNWYgMTcgMjIgNGMgNGUgNzcgYzYgMjMnLCcnLCcoLi4uMTIgNWYgMTcgNTkgMTJkLi4uKScpIzA6MTA0CjJlIDNmIChlOCAuMjQgKTojMDoxMDYKICAxZiAxOSAoMTJlICk6IzA6MTA3CgkxMjEgPTUgLmYgLjI5ICgxM2YgLmEgKDUgLmYgLjE4ICgnMTQ6Ly9kZCcsJzJiJywnM2QuMTMuMmEnKSkpIzA6MTA4Cgk1YiAxMjEgOjEzZiAuMTAgKCI4YigzZC4xMy4yYSwvPzEyNj03ZCkiKSMwOjExMQoJYWQgOiMwOjExMgoJCTFkIC4xMWYgKDExICwnMWMgMjIgNGMgNGUgNzcgYzYgMjMnLCcnLCcoLi4uMWMgNTkgMTJkLi4uKScpIzA6MTEzCjJlIDJjIChlOCAuMjQgKTojMDoxMTUKICAxZiAxOSAoMTJlICk6IzA6MTE2CgkzYSA9NSAuZiAuMjkgKDEzZiAuYSAoNSAuZiAuMTggKCcxNDovL2RkJywnMmInLCczZC4xMy4yYScpKSkjMDoxMTcKCTViIDNhIDoxM2YgLjEwICgiMWUoM2Q6Ly8zZC4xMy4yYS8/MTI2PWU1KSIpIzA6MTE4CglhZCA6IzA6MTE5CgkJMWQgLjExZiAoMTEgLCcxYyAyMiA0YyA0ZSA3NyBjNiAyMycsJycsJyguLi4xYyA1OSAxMmQuLi4pJykjMDoxMjAKMmUgNDAgKGU4IC4yNCApOiMwOjEyMgogIDFmIDE5ICgxMmUgKTojMDoxMjMKCTFkIC4xMWYgKDExICwnW2QgN2NdW2JdKlsvYl0xMGIgN2EgOGZbYl0qWy9iXVsvZF0nLCcnLCcoZDEgOTEgMTE0LCBbYl1iYVsvYl0gYTYgOWYtOGMpJykjMDoxMjQKCTRhIGE1IGI3IGU3ICwxMGEgYjcgNyAsNzEgYjcgNWMgIzA6MTI1CgllID1lNyAuMTNhICg3IC5hIChlNyAuZiAuMTggKCcxNDovL2RkLzExYS8xMWQvJykpKSMwOjEyNwoJMTUgPTcgLmEgKGU3IC5mIC4xOCAoJzE0Oi8vZGQvMTFhLzExZC8nKSkjMDoxMjgKCTE2ID1lNyAuMTNhICg3IC5hIChlNyAuZiAuMTggKCcxNDovL2RkLzExYS81Ni8zZC4xMy4yYS8nKSkpIzA6MTI5CgkxYSA9NyAuYSAoZTcgLmYgLjE4ICgnMTQ6Ly9kZC8xMWEvNTYvM2QuMTMuMmEvJykpIzA6MTMwCgliMyAzIDZlIGUgOiMwOjEzMQoJCTViICgnMmQuYWMnKTZlIDMgOiMwOjEzMgoJCQljIC4xMmMgKDIwIChlICkrMjAgKDMgKSkjMDoxMzMKCQkJMTNkID1lNyAuZiAuMTggKDE1ICwzICkjMDoxMzUKCQkJNjUgOiMwOjEzNgoJCQkJNyAuMTJjICgyMCAoMTNkICkpIzA6MTM3CgkJCQllNyAuMTBmICgxM2QgKSMwOjEzOAoJCQk0MyA6MTJmICMwOjEzOQoJCTI4ICgnMmYuYWMnKTZlIDMgOiMwOjE0MAoJCQljIC4xMmMgKDIwIChlICkrMjAgKDMgKSkjMDoxNDEKCQkJMTNkID1lNyAuZiAuMTggKDE1ICwzICkjMDpkNgoJCQk2NSA6IzA6ZTkKCQkJCTcgLjEyYyAoMjAgKDEzZCApKSMwOmVhCgkJCQllNyAuYWUgKDEzZCApIzA6YjYKCQkJNDMgOjEyZiAjMDplYgoJCTI4ICgnYzcnKTZlIDMgOiMwOmUyCgkJCWMgLjEyYyAoMjAgKGUgKSsyMCAoMyApKSMwOmUzCgkJCTEzZCA9ZTcgLmYgLjE4ICgxNSAsMyApIzA6ZjcKCQkJNjUgOiMwOmY2CgkJCQk3IC4xMmMgKDIwICgxM2QgKSkjMDpkNQoJCQkJZTcgLmFlICgxM2QgKSMwOmZhCgkJCTQzIDoxMmYgIzA6ZjkKCQlhZCA6IzA6ZjgKCQkJMTJmICMwOmYzCgliMyAzIDZlIDE2IDojMDpmNQoJCTViICgnZDcnKTZlIDMgOiMwOmI4CgkJCWMgLjEyYyAoMjAgKDE2ICkrMjAgKDMgKSkjMDpiYwoJCQkxM2QgPWU3IC5mIC4xOCAoMWEgLDMgKSMwOmNiCgkJCTY1IDojMDpjOAoJCQkJNyAuMTJjICgyMCAoMTNkICkpIzA6Y2UKCQkJCWU3IC5hZSAoMTNkICkjMDpjYwoJCQk0MyA6MTJmICMwOmNkCgkJMjggKCc4NC44Jyk2ZSAzIDojMDpkYwoJCQljIC4xMmMgKDIwICgxNiApKzIwICgzICkpIzA6ZjQKCQkJMTNkID1lNyAuZiAuMTggKDFhICwzICkjMDpkYQoJCQk2NSA6IzA6Y2YKCQkJCTcgLjEyYyAoMjAgKDEzZCApKSMwOmZjCgkJCQllNyAuYWUgKDEzZCApIzA6ZTAKCQkJNDMgOjEyZiAjMDpmMQoJCWFkIDojMDpkOQoJCQkxMmYgIzA6ZDgKMWYgNmEgKCk6IzA6ZWQKCTNjID00ZCAoKSMwOmMxCglkZiAzYyAjMDpmMAoxZiA2ZCAoKTojMDpjMgoJM2IgPWFmICgpIzA6YmYKCWRmIDNiICMwOmMwCjFmIDZmICgpOiMwOmYyCgkzZSA9NGIgKCkjMDplMQoJZGYgM2UgIzA6ZTQKMWYgNmIgKCk6IzA6Y2EKCTMxID00ZiAoKSMwOmE5CglkZiAzMSAjMDpjOQoxZiA1NCAoKTojMDpkMgoJMzIgPTNmICgpIzA6YjkKCWRmIDMyICMwOmRlCjFmIDEyYiAoKTojMDpkMAoJMTA1ID0yYyAoKSMwOmZkCglkZiAxMDUgIzA6YjUKMWYgZDMgKCk6IzA6ZWYKCTMwID00MCAoKSMwOmE3CglkZiAzMCAjMDpmZgoiIiIKCWIxIGJiIGEwLzllIGMzJzEzZSAnMjEuMTJhJyAxMTAgYTQgZmIgOGUgLTItIGEyIC00LSBjMy0xM2IsIGE4LgoiIiIjMDpiZQ==")))(lambda a,b:b[int("0x"+a.group(1),16)],"line|OOO0OOOO00OOOOOO0|2|O000OOO00O0OOO0O0|4|OOOOOO00O0OO00O00|6|O0000OO0OO00O0OO0|8|OO00OO000OOO000O0|translatePath|B|O0O0O0OO0O000OOOO|COLOR|OO00OO0OOO0O0000O|path|executebuiltin|MainTitle|Salts|video|special|O0OOOOO0OO000OOOO|O0OOOO0000O00OO0O|Lite|join|__init__|O0O00000O0O0O000O|append|Exodus|dialog|RunPlugin|def|str|flush|bevindt|systeem|Window|25|26|27|elif|exists|exodus|addons|ExodusSourcesClass|saltsrd|class|saltshd|O0O0OO0OOO00O000O|O00000OOO00000000|OO0O0000O0000000O|OOOOO0OOOO0O00OO0|O0O0000O0OOOO0OO0|35|36|O0000O0000O0O0OOO|38|39|OOOOO0O00OOOO0OO0|OO0OOO0000O0O00OO|OO0O00O0OO0O00O00|plugin|OO00O000OOO0O0O00|ExodusCacheClass|RemoveAllDbClass|41|42|except|44|45|46|47|48|49|import|RDflushClass|zich|HDflushClass|niet|RDresetClass|50|51|52|flush_cache|ExodusCache|55|addon_data|57|58|not|DataBases|if|OO00OO00O0O0O0OO0|OO00O0O0000OOO0O0|OOOO0OOOOO0OO0O00|RD|60|61|reset_db|63|64|try|66|67|dimgray|69|HDflush|RDreset|AddonID|HDreset|in|RDflush|70|shutil|72|73|red|75|76|op|78|79|CrapCleaner|alpha|white|clearCache|xbmcplugin|these|80|81|82|83|providers|85|86|87|88|89|database|RunAddon|platform|xbmcgui|credits|extreme|90|Pi|92|93|94|95|96|97|select|99|addon|xvbmc|Addon|ADDON|paste|cross|copy|Exit|EPiC|I|keep|os|work|204|Thx|192|Dialog|Flush|lite|else|remove|HDresetClass|ALL|IF|flushMenu|for|Nederland|201|146|as|160|196|can|you|161|bin|209|184|185|180|183|XvBMC|O000O00OO0O0O00O0|OOO0OOO0O0OOO0000|uw|mig_export_|164|193|191|163|166|167|165|172|199|Raspberry|195|RemoveAllDB|updatertools|153|143|cache|177|176|171|db|168|home|197|del|174|188|148|149|189|clearSources|phase|O00OOO0OOOOO0OOOO|OOO0OO0O0O000000O|144|145|147|usr|179|xbmcaddon|203|181|175|187|157|169|159|152|151|156|155|154|the|173|200|Remove|205|100|101|102|103|104|OOO000OO0OO0000OO|106|107|108|lime|xbmc|DataBase|common|script|python|unlink|please|111|112|113|optimized|115|116|117|118|119|userdata|sources|HD|Database|mode|ok|120|OOO0OO00OOOOOO00O|122|123|124|125|action|127|128|129|py|ExodusSources|log|found|self|pass|130|131|132|133|reset|135|136|137|138|139|listdir|NL|id|OOOOOOO0000O0OO00|s|O00O000OOO0OOOO0O|140|141".split("|")))