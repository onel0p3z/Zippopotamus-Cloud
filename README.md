# Zippopotamus Cloud

---

## New Management

Zippopotam.us has been taken over and re-launched.

For now, the primary concern was getting it back up on stable hosting.

I look forward to adding some features including caching and variable nearby query distances, etc in the near future.

I'm very grateful to Samir and Jeff for cooperating in this transition, and their original work for this project.

Please dont hesitate to contact me with any questions, comments, or concerns.  You can file an issue on this repository, or you may email me at [trea@treahauet.com](mailto:trea@treahauet.com).

Thanks,

[Trea Hauet](http://treahauet.com)

---

This is a repository for  [Zippopotamus](http://www.zippopotam.us) the global postal code API

If you want to contribute to the improving the site, back-end, front-end etc. Just fork away and submit pull requests. 

### Sample Implementations 

Checkout the `static/` folder to see some of the sample implementations of Zippopotamus for inspiration and examples for how to implement Zippopotamus API for use in your website etc.

If you want to share an implementation, we would love to post example cases of Zippopotamus on our homepage.

### Response Format

On May 1st Zippopotamus changed their JSON response format to work better with international postal codes.  Now we support a one-to-many format service. That is that one zip code may map to many regions, this is common in countries like Spain and France (but not in the US and Germany). 

## Postal Code Information

For now, I'm looking at the best possible way to collaborate on any additional postal code information.  Information coming soon.

## Technical Information

### What is Zippopotamus built on

At the moment the zippopotamus is built on Python, MongoDB and bottle.py framework.

### Local Testing?

The site is configured to run on Apache mod_wsgi, if you want to test out the web interface you can change the wsgi.py file to include the last commented line, which is used to run the site on your local host.

### Suggestions and Comments?

Open an issue if you have any questions, comments, or concerns.