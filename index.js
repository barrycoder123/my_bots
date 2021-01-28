const discord = require("discord.js");
const config = require("./config.json");
const fs = require("fs"); 
const randomPuppy = require('random-puppy');
const fetch = require('node-fetch');
const querystring = require('querystring');
const bot = new discord.Client({disableEveryone: true});

bot.on("ready", async () => {
    console.log(`${bot.user.username} is ready for action!`);
    bot.user.setActivity("Minecraft");
});

bot.on("message", async message =>{
  const prefix = config.prefix;
  if (!message.content.startsWith(prefix) || message.author.bot) return;
    // if(message.channel.type === "dm") return;

  const args = message.content.slice(prefix.length).trim().split(/ +/);
  const command = args.shift().toLowerCase();

  if (command === 'cat') {
		const { file } = await fetch('https://aws.random.cat/meow').then(response => response.json());

		message.channel.send(file);
	} else if (command === 'meme') {
    let reddit = [
      "mathmemes",
      "animemes",
      "animememes",
      "programmerhumor",
      "comedycemetry",
      "meme",
      "dankmemes",
      "funny",
      "teenager",
      "historymemes",
      "lastimages",
      "comedyheaven",
      "pewdiepiesubmissions"
    ]

    let subreddit = reddit[Math.floor(Math.random() * reddit.length)];

    message.channel.startTyping();

    randomPuppy(subreddit).then(async url => {
            await message.channel.send({
                files: [{
                    attachment: url,
                    name: 'meme.png'
                }]
            }).then(() => message.channel.stopTyping());
    }).catch(err => console.error(err));

  } else if (command.toLowerCase() === 'urbandict') {
    console.log("here");
    if (!args.length) {
      return message.channel.send('You need to give me a word to look up');
    }
    
    // the command argument to query eg) !urbanDict {args.join()}
    const query = querystring.stringify({ term: args.join(' ') });

    const { list } = await fetch(`https://api.urbandictionary.com/v0/define?${query}`).then(response => response.json());

    // check if any answers were returned: 
    if (!list.length) {
      return message.channel.send(`No results found for **${args.join(' ')}**.`)
    }

    // send the defintion:
    message.channel.send(list[0].definition);
  }
});

bot.login(config.token);