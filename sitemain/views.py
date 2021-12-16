from django.shortcuts import render
from django.http import HttpResponseNotFound


def view_homepage(request):

  return render( request, 'sitehome.html' )


def view_resume(request):


  experience_data = [
      {
        'year' : '08/2020 - Present',
        'detail' : {
          'role' : 'Senior Solutions Architect',
          'organization' : 'Navagis Asia Pacific PTE. LTD.',
          'org_desc' : 'Google Cloud Premier Partner and Location Intelligence company',
          'website' : 'https://navagis.com/',
          'duties' : [
            'Develops web based Geographic Information Systems using PHP, HTML, CSS, Javascript, React, Angularjs, Python, PostgreSQL, CesiumJS and Google Maps API',
            'Assists in deployment of updates to cloud-based servers'
          ],
          'tech' : ['HTML', 'CSS', 'Javascript', 'PHP', 'Python', 'Bash', 'Node.js', 'Angularjs', 'React', 'Linux', 'REST', 'Postgresql', 'Cesiumjs', 'Google Maps Api'],
          'org_picture' : 'navagis-logo.svg'
        }
       },

       {
        'year' : '09/2016 - 06/2019',
        'detail' : {
          'role' : 'Web Application Developer',
          'organization' : 'Inspire Education Services, Inc.',
          'org_desc' : 'Australia-based online training and education firm',
          'website' : 'https://www.inspireeducation.net.au/',
          'duties' : [
            'Maintained and developed features for the company web application',
            'Designed RESTful API framework for inter-application operability',
            'Optimized SQL queries for faster transactions',
            'Implemented the use of 3rd-party search and logging applications',
            ],
          'tech' : ['HTML', 'css', 'Javascript', 'JQquery', 'PHP', 'MySQL', 'Linux', 'Bash', 'Moodle', 'Sphinx Search', 'REST', 'OOP'],
          'org_picture' : 'inspire-logo.png'
        }
       },


       {
        'year' : '02/2011 - 03/2016',
        'detail' : {
          'role' : 'Web Application Developer',
          'organization' : 'Chikka Philippines, Inc.',
          'org_desc' : 'Telecommunications software solutions company',
          'website' : '',
          'duties' : [
            'Developed large-scale web applications in a team for both front-end and back end using Python TornadoWeb, MySQL, Redis, ZMQ and other technologies.',
            'Led a small team in developing a mini web store'
          ],
          'tech' : ['HTML', 'CSS', 'Javascript', 'JQuery', 'Python', 'TornadoWeb', 'MariaDB', 'Linux', 'Sphinx Search', 'REST', 'ZMQ', 'Redis', 'OOP'],
          'org_picture' : 'chikka-logo.svg'
        }
       },

       {
        'year' : '11/2007 - 06/2010',
        'detail' : {
          'role' : 'Web Application Developer',
          'organization' : 'Yellowasp Web Services',
          'org_desc' : 'Web development outsourcing firm',
          'website' : '',
          'duties' : [
          'Developed corporate websites for foreign clients using Drupal 6.',
          'Directly worked with account manager to implement client requests.'
          ],
          'tech' : ['HTML', 'CSS', 'Javascript','PHP', 'Drupal', 'JQuery', 'MySQL', 'Linux'],

          'org_picture' : 'yellowasp-logo.png'
        }
       },


       {
        'year' : '02/2004 - 11/2007',
        'detail' : {
          'role' : 'Junior Network Administrator',
          'organization' : 'Mod.Net.PH / PHCOLO',
          'org_desc' : 'Internet Service and Network Security Provider',
          'website' : 'https://www.phcolo.ph/',
          'duties' : [
          'Aided in maintaining the local network infrastructure of the company.',
          'Configured network routers and switches for clients',
          'Managed domian name servers and network monitoring tools such as nagios and mrtg'
          ],
          'tech' : ['HTML', 'CSS', 'javascript', 'linux'],
          'org_picture' : 'phcolo-logo.png'
        }
       },       
    ]
  
  skills_list = {}
  for detail  in experience_data:
    for tech  in detail['detail']['tech'] :
      skills_list[tech] = 1
  
  skills_list = skills_list.keys()

  return render( request, 'my_resume.html', {'exp_data': experience_data, 'skills_list':skills_list } )
