@echo off
echo ========================================
echo   Nettoyage Docker
echo ========================================

echo.
echo [1/5] Arret des conteneurs non essentiels...
docker stop metabase 2>NUL
docker stop superset 2>NUL

echo.
echo [2/5] Suppression des conteneurs arretes...
docker container prune -f

echo.
echo [3/5] Suppression des images non utilisees...
docker image prune -a -f

echo.
echo [4/5] Suppression des volumes non utilises...
docker volume prune -f

echo.
echo [5/5] Suppression du cache de build...
docker builder prune -a -f

echo.
echo ========================================
echo   Nettoyage termine !
echo ========================================
echo.

docker system df

pause