//Script taken from "Traversy Media"
//https://youtu.be/ksXwaWHCW6k

const cacheName = 'v1';
const chacheAssets = [
    'index.html',
    'manifest.json',
    '/css/style.css',
    '/scripts/main.js',
    '/Images/WebsiteBackgrounds/Top Down View.WebP',
    '/Images/WebsiteBackgrounds/PHS\ Background.WebP',
    '/Images/WebsiteText/School Comparison 3D Model.WebP',
    '/Images/WebsiteText/School\ Comparison\ 3D\ Model\ Real.WebP',
    '/Images/WebsiteLogo/Squirrel Logo 512.WebP'
];

self.addEventListener('install', (e) => {
    console.log('Service Worker: Installed');

    e.waitUntil(
        caches
            .open(cacheName)
            .then(cache => {
                console.log('Service Worker: Chaching Files');
                cache.addAll(chacheAssets);
            })
            .then(() => self.skipWaiting())
    );
});

self.addEventListener('activate', (e) => {
    console.log('Service Worker: Activated');
    e.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cache => {
                    if (cache !== cacheName) {
                        console.log('Service Worker: Clearing Old Cache');
                        return caches.delete(cache);
                    }
                })
            )
        })
    );
});

self.addEventListener('fetch', e => {
    console.log('Service Worker: Fetching');
    e.respondWith(fetch(e.request).catch(() => caches.match(e.request))
    )
})
