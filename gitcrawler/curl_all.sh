max=100000
echo $cmd  > repos.txt
for i in {1..100000}
do
   cmd=`curl -s https://api.github.com/orgs/openstack/repos?page=$i | grep clone_url | awk -F ":" '{print $2":"$3}'| sed 's/"//g' | cut -d ',' -f 1 | tr -d ' '`
   echo $cmd
   if [ "$cmd" == "" ];then    echo NULL;break; fi
   echo $cmd  >> repos.txt 
done
cat repos.txt  | tr " " "\n" > repos.txt
