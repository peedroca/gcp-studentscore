require('dotenv').config();
const { Client, GatewayIntentBits } = require('discord.js');
const client = new Client({ intents: [
    GatewayIntentBits.Guilds, 
    GatewayIntentBits.GuildMessages, 
    GatewayIntentBits.MessageContent] 
});

client.once('ready', () => {
    console.log('O bot está online!');
});

client.on('messageCreate', message => {
    if (message.content === '!hello') {
        message.channel.send('world');
    }
});

client.login(process.env.DISCORD_BOT_TOKEN)
