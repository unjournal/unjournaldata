import requests
import json
from Crypto.Hash import keccak

class Pubshelper:
    def __init__(self, community_url="https://unjournal.pubpub.org", community_id="d28e8e57-7f59-486b-9395-b548158a27d6", email='revwr@gmail.com',password = '8paswortt' ):
        self.community_url = community_url
        self.community_id = community_id
        self.cookieJar = None
        self.logged_in = False
        self.email = email
        self.password = password



    def login(self):
        k = keccak.new(digest_bits=512)
        k.update(self.password.encode())
        response = requests.post(
            url=f'{self.community_url}/api/login',
            headers={ "accept": "application/json",
                      "cache-control": "no-cache",
                      "content-type": "application/json",
                      "pragma": "no-cache"
                     },
            data=json.dumps({
                'email': self.email,
                'password': k.hexdigest(),

            }),
        )

        self.cookieJar=response.cookies


        if not self.cookieJar:
            raise Exception(f'Login failed, with status {response.status_code}: {response.text}')

        self.logged_in = True

    def authed_request(self, path, method='GET', body=None, options=None, additioalHeaders=None):

            response = requests.request(
                method,
                f'{self.community_url}/api/{path}',
                data=json.dumps(body) if body else None,
                cookies=self.cookieJar,
                headers={ "accept": "application/json",
                      "cache-control": "no-cache",
                      "content-type": "application/json",
                      "pragma": "no-cache",
                      "origin": self.community_url
                      **(additioalHeaders if additioalHeaders else {})
                     },
                **options if options else {},
            )

            if response.status_code < 200 or response.status_code >= 300:
                raise Exception(
                    f'Request failed with status {response.status_code}: {response.text}'
                )

            return response.json()

    def logout(self):
        response =  self.authed_request('logout', 'GET')
        self.cookieJar = None
        self.logged_in = False
        print('Succesfully logged out')

    def get_many_pubs(self, limit = 50, offset = 0, ordering= {'field': 'updatedDate', 'direction': 'DESC'} ,collection_ids=None ,pub_ids=None):

        response = self.authed_request(
            'pubs/many',
            'POST',
            {
                'alreadyFetchedPubIds': [],
                'pubOptions': {
                    'getCollections': True,
                },
                'query': {
                    'communityId': self.community_id,
                    **( {'collectionIds': collection_ids} if collection_ids else {}),
                    **(   {'withinPubIds': pub_ids} if pub_ids else {}),
                    'limit': limit,
                    'offset': offset,
                    'ordering': ordering,
                },
            },
        )

        return response

    def get_byreleased_pubs(self,
                            limit = 50,
                            offset = 0,
                            ordering= {'field': 'updatedDate', 'direction': 'DESC'} ,
                            isReleased=False,
                            collection_ids=None ,
                            pub_ids=None,
                            alreadyFetchedPubIds=[],
                            relatedUserIds =[]
                            ):

        response = self.authed_request(
            'pubs/many',
            'POST',
            {
                'alreadyFetchedPubIds': alreadyFetchedPubIds,
                'pubOptions': {
                    'getCollections': True,
                },
                'query': {
                    'communityId': self.community_id,
                    isReleased: isReleased,
                    **( {'collectionIds': collection_ids} if collection_ids else {}),
                    **(   {'withinPubIds': pub_ids} if pub_ids else {}),
                    'limit': limit,
                    'offset': offset,
                    'ordering': ordering,
                    **(   {'relatedUserIds': relatedUserIds} if relatedUserIds else {}),
                },
            },
        )

        return response


    def delete_pub(self, pub_id):
        response =  self.authed_request(
            path='pubs',
            method='DELETE',
            body={
                'pubId': pub_id,
                'communityId': self.community_id,
            },
        )
        return response

    def getPub(self, pub_id):
        return self.get_many_pubs(pub_ids=[pub_id])
