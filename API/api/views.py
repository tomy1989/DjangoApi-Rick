from os import stat
from posixpath import split
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .CsvHelper import CsvHelper
from . import utils
from collections import namedtuple
from .serizalizers import ResponseSerializer
from .RicknMortyHelper import RicknMortyHelper

UserResponse = namedtuple('Response', ('characters', 'result'))

def get_rick_morty(characters_ids=None, first_id=None, second_id=None):
    #if characters_ids is none user possible pass id by /
    if characters_ids is None:
        if isinstance(first_id, int) and isinstance(second_id, int):
            characters_ids = [first_id, second_id]
        else:
            raise TypeError('Bad arguments pass, only numbers')
            
    else:
        if len(characters_ids) < 3:
            raise ValueError(utils.WRONG_INPUT_LISTID)
        #split by comma to list (we have string list)
        characters_ids = characters_ids.split(',')
        #make int 
        characters_ids = map(int,characters_ids)
        # to a list element
        characters_ids = list(characters_ids)
    #make sure not asking for same id
    if len(set(characters_ids)) != len(characters_ids):
        raise ValueError({utils.WRONG_INPUT_SAMEID})
    RicknMorty = RicknMortyHelper(characters_ids)
    #RicknMorty.drop_data() #used to drop all
    return RicknMorty.GetCompare()

@api_view(['GET'])
def getCompare(request,characters_ids=None, first_id=None, second_id=None): #characters_ids
    try:
        result_dict, character_list = get_rick_morty(characters_ids=characters_ids, first_id=first_id, second_id=second_id) 
        user_response = UserResponse(
            characters = character_list,
            result = result_dict
        )
        
        serializer = ResponseSerializer(user_response)    
        
        return Response(serializer.data)
    except (ValueError, TypeError) as error:
         return Response({'Error msg': str(error)},status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'Something went wrong more information': str(e)}, status=status.HTTP_400_BAD_REQUEST)

"""
    View for req view CSV
"""
@api_view(['GET'])
def getCompareCsv(request,characters_ids=None, first_id=None, second_id=None):
    try:
        print(characters_ids , first_id, second_id)
        result_dict, character_list = get_rick_morty(characters_ids=characters_ids, first_id=first_id, second_id=second_id)
        csv = CsvHelper(result_dict, character_list)
        file_path = csv.create_csv()
        return Response({'file':file_path},status=status.HTTP_200_OK)
    except (ValueError, TypeError) as error:
         return Response({'Error msg': str(error)},status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'Something went wrong more information': str(e)}, status=status.HTTP_400_BAD_REQUEST)
