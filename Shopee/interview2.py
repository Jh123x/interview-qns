# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

print("Hello, world!")


# 
# Old Content below(Python 2):
# 
# # Libraries Included:
# # Numpy, Scipy, Scikit, Pandas
# 
# print "Hello, world!"
# 
# """
# 
# URL Shortener
# 
# https://shopee.sg/item/Apple-iPhone-12-Pro-Max-Graphite-Black-512GB-209730298134-9230390538954?tracking_id=0923jd092_092j3023
# 
# https://sho.rt/28Xkamx1
# 
# https://hbr.org/5-Ways-To-Disappoint-Your-Boss-10934502834-320959203453
# 
# https://sho.rt/xa01iu3R
# 
# 1) shorten(long_url) --> short_url
# 2) resolve(short_url) --> long_url
# 
# ---
# 
# no expiry
# 
# """

class Shorterner(object):
    def __init__(self, domain_name:str):
        """The main shorterner object"""
        self._inverted_lookup = {}
        self.domain = domain_name
        self._lookup_table = {}
        self.start = 0
        
    def keygen(self):
        """Generate keys O(1)"""
        self.start += 1 #No need to worry abt overflow
        #Can do a hash here to make it seem more random
        return str(self.start)
        
    def shortern(self, long_url:str) -> str:
        """Shortern the long url to the short url"""
        
        #Check if URL already exists
        result = self._inverted_lookup.get(long_url, None)
        
        #If it exists, give the cached link
        if(result != None):
            return self._generate_link(result)
        
        #Generate key for the domain
        key = self.keygen()
        
        #Store key,value in lookup table (Can be abstracted into BiMap class)
        self._lookup_table[key] = long_url
        self._inverted_lookup[long_url] = key
        
        #Return shorterned name
        return self._generate_link(key)
    
    def resolve(self, short_url:str) -> str:
        """Resolve the short url to the long url"""
        
        #Get the key
        key = short_url[len(self.domain):]
        
        #Lookup the table
        url = self._lookup_table.get(key, "error")
        
        #Return the actual URL
        return url
    
    def _generate_link(self, key:str) -> str:
        """Generate the web link based on the key"""
        return f"{self.domain}{key}"


if __name__ == "__main__":
    shorterner = Shorterner("http://sho.rt/")

    url1 = "https://shopee.sg/item/Apple-iPhone-12-Pro-Max-Graphite-Black-512GB-209730298134-9230390538954?tracking_id=0923jd092_092j3023"
    
    url2 = "https://hbr.org/5-Ways-To-Disappoint-Your-Boss-10934502834-320959203453"
    
    url3 = "https://shopee.sg/example_url"
    
    
    s1 = shorterner.shortern(url1)
    s2 = shorterner.shortern(url2)
    s3 = shorterner.shortern(url3)
    s4 = shorterner.shortern(url3)
    
    print(f"URL 1: {url1}")
    print(f"URL 2: {url2}")
    print(f"URL 3: {url3}")
    print(f"URL 4: {url3}")
    
    print(f"Shorterned URL 1: {s1}")
    print(f"Shorterned URL 2: {s2}")
    print(f"Shorterned URL 3: {s3}")
    print(f"Shorterned URL 4: {s4}")
    
    r1 = shorterner.resolve(s1)
    r2 = shorterner.resolve(s2)
    r3 = shorterner.resolve(s3)
    r4 = shorterner.resolve(s4)
    
    print(f"Resolved s1 same as url: {r1 == url1}")
    print(f"Resolved s2 same as url: {r2 == url2}")
    print(f"Resolved s3 same as url: {r3 == url3}")
    print(f"Resolved s4 same as url: {r4 == url3}")
    print(f"s3 and s4 equal: {r3 == r4}")


    """
    Server A generate a key -> query C to check if key is used 
    Server B
    
    """





