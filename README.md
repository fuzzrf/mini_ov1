MiniDLNA stack overflow

Project url - http://minidlna.sourceforge.net/

Used in many wifi routers.

There is a stack overflow in SendContainer function.

```

SendContainer(struct upnphttp *h, const char *objectID, int itemStart, int itemCount, char *anchorItem,
              int anchorOffset, int recurse, char *sortOrder, char *filter, unsigned long int randomSeed)
{
	...
	
						short title_state = 0;
                        item = strtok_r(sortOrder, ",", &saveptr);
                        while( item != NULL )
                        {
                                int reverse=0;
                                if( *item == '!' )
                                {
                                        reverse = 1;
                                        item++;
                                }
                                if( strcasecmp(item, "Type") == 0 )
                                {
                                        strcat(order, "CLASS");
                                        strcat(order2, "CLASS");
                                }
						...
}
```

Basically it parses input string and calls strcat() in a loop.

How to verify:
```
1) download minidlna-1.3.0
2) build with asan and tivo support (--enable-tivo)
3) edit minidlna.conf and turn on tivo support (enable_tivo=yes)
4) run minidlnad:
$ ./minidlnad -d -f minidlna.conf

5) run t1.py
```

Asan log attached.

