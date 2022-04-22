import requests
from .serizalizers import ResultSerializer, CharacterSerializer
from charachters.models import Character,Result
import itertools

class RicknMortyHelper:

    def __init__(self, characters_ids):
        self.characters_ids= characters_ids
    
    """
        Function return compare resuslt + characters list 
        doing compare between characters in characters_id list
        if found already existing compare return his data 
        if not exist getting characters and compare them + save to db
    """
    def GetCompare(self):
        try:
            result_search =  Result.objects.get(characters__exact=self.characters_ids)
        
            #if we found in db already compare data
            print('Found already in db')
            serializer = ResultSerializer(result_search, many=False)
            characters_search = list(Character.objects.filter(id__in=self.characters_ids))
            return serializer.data, characters_search
        except:
            #make sure we have in db our characters
            self.getCharacters()
            
            characters_search = list(Character.objects.filter(id__in=self.characters_ids))
            comp = self.__compare(characters_search)
            compare_result = Result(result = comp,characters = self.characters_ids)
            compare_result.save()
            serializer = ResultSerializer(compare_result)
            return serializer.data, characters_search#compare_result
        
    
    
    """
        Function to get character from rick url api and save them in our db 
        but before delete existing charcters from characters_id list
    """
    def getCharacters(self): 
        
        Character.objects.filter(id__in=self.characters_ids).delete()
        #getting characters from rick api
        ids = ','.join(map(str,self.characters_ids))
        re = requests.get('https://rickandmortyapi.com/api/character/' + ids)
        re_data =re.json()
        if len(re_data) != len(self.characters_ids):
            raise Exception('Some characters are missing try again')
        if re.status_code != 200:
            raise Exception('got problem with rickandmortyapi.com response')
        serialized = CharacterSerializer(data=re_data, many=True)
        if serialized.is_valid(raise_exception=True):
            serialized.save()
            #print(serialized.data)
            return serialized.data
    
    """
        Private function to compare in list of characters identical by generating all compare combination using intertool
    """
    def __compare(self, characters_search):
        for a, b in itertools.combinations(characters_search, 2):
            if a != b:
                return False
        return True
    """
        Made this function just for me to drop sometimes table without access manage.py shell for it
    """
    def drop_data(self):
        Character.objects.all().delete()
        Result.objects.all().delete()
        
        