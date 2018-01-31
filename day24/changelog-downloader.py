import urllib.request


base_urls = ['https://cdn.changelog.com/uploads/podcast/<id>/the-changelog-<id>.mp3',
             'https://cdn.changelog.com/uploads/gotime/<id>/go-time-<id>.mp3',
             'https://cdn.changelog.com/uploads/rfc/<id>/request-for-commits-<id>.mp3',
             'https://cdn.changelog.com/uploads/founderstalk/<id>/founders-talk-<id>.mp3',
             'https://cdn.changelog.com/uploads/spotlight/<id>/spotlight-<id>.mp3',
             'https://cdn.changelog.com/uploads/jsparty/<id>/js-party-<id>.mp3',
            ]


def download_podcast(n):
    base_url = base_urls[n - 1]
    print("Enter one or more episodes to download:")
    episodes = (int(x) for x in input().split(','))
    target = '/home/philipp/Downloads/'

    for episode in episodes:
        download_url = base_url.replace('<id>', str(episode))
        print('Downloading episode {} to {}'.format(str(episode),target))
        try:
            urllib.request.urlretrieve(download_url, target + download_url.split('/')[-1])
            print('Download complete!')
        except:
            print('Could not download file: {}'.format(download_url))



def main():
    print('Which podcast would you like to download?')
    print('(1) - The Changelog')
    print('(2) - Go Time')
    print('(3) - Request for Commits')
    print('(4) - Founders Talk')
    print('(5) - Spotlight')
    print('(6) - JS Party')

    n = int(input())
    download_podcast(n)


if __name__ == "__main__":
    main()
