require('dotenv').config();
const { Client, GatewayIntentBits, ChannelType } = require('discord.js');
const axios = require('axios');
const client = new Client({ intents: [
    GatewayIntentBits.Guilds, 
    GatewayIntentBits.GuildMessages, 
    GatewayIntentBits.MessageContent,
    GatewayIntentBits.DirectMessages,  
    GatewayIntentBits.DirectMessageReactions,
    4096
]});

const endpoint = "https://savemessage-uicelghxba-uc.a.run.app/"

client.once('ready', () => {
    console.log('O bot está online!');
});

client.on('messageCreate', message => {
    if (message.content === '!join') {
        message.author.send('Hey bro! What\'s up?');
    }

    if (message.author.bot) return;

    if (message.channel.type === ChannelType.DM) {
        const params = {
            author: message.author.username,
            code: process.env.CODE, 
            response: message.content
        };
        
        axios.get(endpoint, { params })
            .then(response => {
                const data = {
                    content: `${message.author.username} Correct Answer! 🎉`
                }
                axios.post(process.env.DISCORD_WEBHOOK_SUCCESS, data)
            })
            .catch(error => {
                console.error(error);
            });// 
    }
});

client.login(process.env.DISCORD_BOT_TOKEN)
