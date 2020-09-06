using System;

namespace Billiards
{
    public static class BilliardsTask
    {
        /// <summary>
        /// 
        /// </summary>
        /// <param name="directionRadians">Угол направелния движения шара</param>
        /// <param name="wallInclinationRadians">Угол</param>
        /// <returns></returns>
        public static double BounceWall(double directionRadians, double wallInclinationRadians)
        {
            //TODO
            Console.WriteLine((((2 * wallInclinationRadians) - directionRadians)*180) / Math.PI);
            return (2 * wallInclinationRadians) - directionRadians;
        }
    }
}