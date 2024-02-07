import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

process.on('SIGINT', () => {
  client.quit();
});

setTimeout(() => {
  console.log('Exiting script after timeout');
  process.exit();
}, 5000);
