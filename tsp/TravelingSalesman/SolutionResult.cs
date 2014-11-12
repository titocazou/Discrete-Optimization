using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TravelingSalesman
{
    /// <summary>
    ///   A solution result for the tsp problem
    /// </summary>
    public class SolutionResult
    {
        /// <summary>
        ///   Constructor
        /// </summary>
        /// <value> The path. </value>
        /* Constructor */
        internal SolutionResult ( List<Node>  path2)
        {
            this.Path= new List<Node>(path2);
        }

        internal SolutionResult ()
        {
            this.Path = new List<Node>();
        }

        /// <summary>
        ///   Gets the total distance of the path.
        /// </summary>
        /// <value> The distance. </value>
        public double Distance
        {
            get
            {
                //double distance = this.Path.Last().DistanceTo(this.Path.First());
                //Parallel.For(1, this.Path.Count - 1, k =>
                //{
                //    distance += this.Path[k].DistanceTo(this.Path[k - 1]);
                //});
                //return distance;

                // get the last leg distance
                var distance = this.Path.Last().DistanceTo(this.Path.First());
                for (int k = 1; k < this.Path.Count; k++)
                {
                    // add in all the intermediate distances
                    distance += this.Path[k].DistanceTo(this.Path[k - 1]);
                }
                return distance;
            }
        }

        /// <summary>
        ///   Gets the path.
        /// </summary>
        /// <value> The path. </value>
        public List<Node> Path
        {
            get;
            set;
        }


        /// <summary>
        ///   Returns a <see cref="System.String" /> that represents the current <see cref="SolutionResult" /> . This conforms to the output format expected in the course.
        /// </summary>
        /// <returns> A <see cref="System.String" /> that represents the current <see cref="SolutionResult" /> . </returns>
        public override string ToString()
        {
            var builder = new StringBuilder();
            builder.AppendLine(Distance.ToString(CultureInfo.InvariantCulture) + " 0");

            foreach (var node in Path)
                builder.Append(node.Index + " ");

            builder.AppendLine("");
            return builder.ToString();
        }
    }
}