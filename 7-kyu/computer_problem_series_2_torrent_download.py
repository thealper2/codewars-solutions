def torrent(files): 
    def download_time(file):
        size_Mb = file['size_GB'] * 1000 * 8
        return size_Mb / file['speed_Mbps']
    
    files_sorted = sorted(files, key=lambda x: (download_time(x), x['name']))
    order = [f['name'] for f in files_sorted]
    last_time = download_time(files_sorted[-1])
    return (order, last_time)
