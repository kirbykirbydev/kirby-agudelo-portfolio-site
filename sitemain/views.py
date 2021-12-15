from django.shortcuts import render
from django.http import HttpResponseNotFound


def view_homepage(request):

  return render( request, 'sitehome.html' )


def view_resume(request):


  experience_data = [
      {
        'year' : '2020 - Present',
        'detail' : {
          'role' : 'Senior Solutions Architect',
          'organization' : 'Navagis Asia Pacific PTE. LTD.',
          'org_desc' : 'Google Cloud Premier Partner and Location Intelligence company',
          'description' : 'Develops geolocation-related solutions for web applications using PHP, HTML, CSS, Javascript, React, Angularjs, Python, PostgreSQL, CesiumJS, Google Maps API',
          'website' : 'https://navagis.com/',
          'org_picture' : 'navagis-logo.svg'
        }
       },

       {
        'year' : '2016 - 2019',
        'detail' : {
          'role' : 'Web Application Developer',
          'organization' : 'Inspire Education Services, Inc.',
          'org_desc' : 'Australia-based online training and education firm',
          'description' : '',
          'website' : 'https://www.inspireeducation.net.au/',
          'duties' : [
          'Maintained and developed features for the company web application',
          'Designed RESTful API framework for inter-application operability',
          'Optimized SQL queries for faster transactions',
          'Implemented the use of 3rd-party search and logging applications',
          ],
          'org_picture' : 'inspire-logo.png'
        }
       },


       {
        'year' : '2011 - 2016',
        'detail' : {
          'role' : 'Web Application Developer',
          'organization' : 'Chikka Philippines, Inc.',
          'org_desc' : 'Telecommunications software solutions company',
          'description' : '',
          'website' : '',
          'duties' : [
            'Developed large-scale web applications in a team for both front-end and back end using Python TornadoWeb, MySQL, Redis, ZMQ and other technologies.',
            'Led a small team in developing a mini web store'
          ],
          'org_picture' : 'chikka-logo.svg'
        }
       },

       {
        'year' : '2007 - 2010',
        'detail' : {
          'role' : 'Web Application Developer',
          'organization' : 'Yellowasp Web Services',
          'org_desc' : 'Web development outsourcing firm',
          'description' : '',
          'website' : '',
          'duties' : [
          'Developed corporate websites for foreign clients using Drupal 6.',
          'Directly worked with account manager to implement client requests.'
          ],
          'org_picture' : 'yellowasp-logo.png'
        }
       },


       {
        'year' : '2004 - 2007',
        'detail' : {
          'role' : 'Junior Network Administrator',
          'organization' : 'Mod.Net.PH / PHCOLO',
          'org_desc' : 'Internet Service and Network Security Provider',
          'description' : '',
          'website' : 'https://www.phcolo.ph/',
          'duties' : [
          'Aided in maintaining the local network infrastructure of the company.',
          'Configured network routers and switches for clients',
          'Managed domian name servers and network monitoring tools such as nagios and mrtg'
          ],
          'org_picture' : 'phcolo-logo.png'
        }
       },       
    ]

  skills_list = [
      'HTML', 'CSS', 'Javascript', 'PHP', 'Python', 'Django', 'Bash', 'Jquery', 'React', 'MySQL', 
    'PostgreSQL', 'Redis', 'Linux', 'Node.js', 'ExpressJS', 'Git', 'SVN', 'OOP', 'MVC', 'REST'
    ]


  return render( request, 'my_resume.html', {'exp_data': experience_data, 'skills_list':skills_list } )